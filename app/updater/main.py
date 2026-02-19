import ctypes
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile

import wx


WAIT_OBJECT_0 = 0x00000000
WAIT_TIMEOUT = 0x00000102
SYNCHRONIZE = 0x00100000
PROCESS_QUERY_LIMITED_INFORMATION = 0x1000


def _wait_for_pid(pid, timeout_s=180):
    if pid <= 0 or os.name != "nt":
        return True
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    open_process = kernel32.OpenProcess
    open_process.argtypes = [ctypes.c_uint32, ctypes.c_int, ctypes.c_uint32]
    open_process.restype = ctypes.c_void_p
    wait_for_single = kernel32.WaitForSingleObject
    wait_for_single.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    wait_for_single.restype = ctypes.c_uint32
    close_handle = kernel32.CloseHandle
    close_handle.argtypes = [ctypes.c_void_p]
    close_handle.restype = ctypes.c_int

    handle = open_process(SYNCHRONIZE | PROCESS_QUERY_LIMITED_INFORMATION, 0, int(pid))
    if not handle:
        return True
    try:
        result = wait_for_single(handle, int(max(0, timeout_s) * 1000))
    finally:
        close_handle(handle)
    return result in (WAIT_OBJECT_0, 0x00000080)


def _focus_window(win):
    if win is None:
        return
    try:
        win.Raise()
    except Exception:
        pass
    try:
        win.SetFocus()
    except Exception:
        pass
    try:
        win.RequestUserAttention()
    except Exception:
        pass
    if os.name == "nt":
        try:
            hwnd = int(win.GetHandle())
            user32 = ctypes.WinDLL("user32", use_last_error=True)
            user32.ShowWindow(hwnd, 5)
            user32.BringWindowToTop(hwnd)
            user32.SetForegroundWindow(hwnd)
        except Exception:
            pass


def _show_message(parent, title, text, style):
    dlg = wx.MessageDialog(parent, text, title, style)
    _focus_window(dlg)
    try:
        return dlg.ShowModal()
    finally:
        dlg.Destroy()


def _payload_root(path):
    entries = [name for name in os.listdir(path) if name not in (".", "..")]
    if len(entries) != 1:
        return path
    root = os.path.join(path, entries[0])
    if os.path.isdir(root):
        return root
    return path


def _iter_files(root):
    for base, _dirs, files in os.walk(root):
        for name in files:
            yield os.path.join(base, name)


def _restart_app(install_dir):
    exe = os.path.join(install_dir, "SimpleAudioPlayer.exe")
    if not os.path.isfile(exe):
        exe = os.path.join(install_dir, "main.exe")
    if not os.path.isfile(exe):
        return
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    try:
        subprocess.Popen([exe], cwd=install_dir, creationflags=flags)
    except Exception:
        return


def _copy_payload(payload_root, install_dir, dlg, start_pct, end_pct):
    files = list(_iter_files(payload_root))
    total = max(1, len(files))
    for idx, src in enumerate(files, start=1):
        rel = os.path.relpath(src, payload_root)
        dst = os.path.join(install_dir, rel)
        if os.path.basename(dst).lower() == "updater.exe":
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        pct = start_pct + int((idx / total) * (end_pct - start_pct))
        keep, _skip = dlg.Update(
            min(100, max(0, pct)),
            f"Replacing files... {idx}/{total}",
        )
        if not keep:
            return False
    return True


def _apply_zip(asset_path, install_dir):
    with zipfile.ZipFile(asset_path, "r") as zf:
        names = [name for name in zf.namelist() if not name.endswith("/")]
        total = max(1, len(names))
        dlg = wx.ProgressDialog(
            "Applying Update",
            "Extracting update...",
            maximum=100,
            style=wx.PD_APP_MODAL | wx.PD_CAN_ABORT | wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME,
        )
        _focus_window(dlg)
        temp_dir = tempfile.mkdtemp(prefix="sap_updater_")
        try:
            for idx, name in enumerate(names, start=1):
                zf.extract(name, temp_dir)
                pct = int((idx / total) * 60)
                keep, _skip = dlg.Update(min(100, max(0, pct)), f"Extracting files... {idx}/{total}")
                if not keep:
                    return False

            root = _payload_root(temp_dir)
            ok = _copy_payload(root, install_dir, dlg, 60, 100)
            if not ok:
                return False
            dlg.Update(100, "Finalizing update...")
            return True
        finally:
            dlg.Destroy()
            shutil.rmtree(temp_dir, ignore_errors=True)


def _run_installer(asset_path, install_dir):
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    subprocess.Popen([asset_path], cwd=install_dir, creationflags=flags)


def _parse_args():
    if len(sys.argv) < 3:
        return "", "", 0
    asset_path = os.path.abspath(sys.argv[1])
    install_dir = os.path.abspath(sys.argv[2])
    pid = 0
    if len(sys.argv) >= 4:
        try:
            pid = int(str(sys.argv[3] or "0"))
        except Exception:
            pid = 0
    return asset_path, install_dir, pid


class UpdaterApp(wx.App):
    def OnInit(self):
        self._host = wx.Frame(None, title="Updater", size=(320, 120))
        self._host.Show()
        _focus_window(self._host)

        asset_path, install_dir, pid = _parse_args()
        if not asset_path or not install_dir:
            _show_message(self._host, "Updater", "Invalid updater arguments.", wx.OK | wx.ICON_ERROR)
            return False
        if not os.path.isfile(asset_path):
            _show_message(self._host, "Updater", "Update package was not found.", wx.OK | wx.ICON_ERROR)
            return False
        if not os.path.isdir(install_dir):
            _show_message(self._host, "Updater", "Install directory is invalid.", wx.OK | wx.ICON_ERROR)
            return False

        if pid > 0:
            _wait_for_pid(pid, timeout_s=300)

        ext = os.path.splitext(asset_path)[1].lower()
        try:
            if ext == ".zip":
                ok = _apply_zip(asset_path, install_dir)
                if not ok:
                    _show_message(self._host, "Updater", "Update was cancelled.", wx.OK | wx.ICON_WARNING)
                    return False
                _restart_app(install_dir)
                _show_message(
                    self._host,
                    "Updater",
                    "Update completed successfully.",
                    wx.OK | wx.ICON_INFORMATION,
                )
                return False

            if ext == ".exe":
                _run_installer(asset_path, install_dir)
                _show_message(
                    self._host,
                    "Updater",
                    "Installer launched successfully.",
                    wx.OK | wx.ICON_INFORMATION,
                )
                return False

            _show_message(
                self._host,
                "Updater",
                "Unsupported update package type.",
                wx.OK | wx.ICON_ERROR,
            )
            return False
        except Exception as exc:
            _show_message(self._host, "Updater", f"Update failed:\n{exc}", wx.OK | wx.ICON_ERROR)
            return False


if __name__ == "__main__":
    app = UpdaterApp(False)
    app.MainLoop()
