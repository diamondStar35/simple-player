import wx
from gettext import gettext as _


AUDIO_WILDCARD = (
    "Audio Files (*.aac;*.aiff;*.alac;*.flac;*.m4a;*.mp3;*.mp4;*.ogg;*.opus;*.wav;*.wma)|"
    "*.aac;*.aiff;*.alac;*.flac;*.m4a;*.mp3;*.mp4;*.ogg;*.opus;*.wav;*.wma|"
    "All Files (*.*)|*.*"
)


def open_file_dialog(parent, initial_dir):
    with wx.FileDialog(
        parent,
        message="",
        defaultDir=initial_dir or "",
        wildcard=AUDIO_WILDCARD,
        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
    ) as dialog:
        if dialog.ShowModal() == wx.ID_OK:
            return dialog.GetPath(), dialog.GetDirectory()
    return None, None


def open_folder_dialog(parent, initial_dir):
    with wx.DirDialog(
        parent,
        message="",
        defaultPath=initial_dir or "",
        style=wx.DD_DIR_MUST_EXIST,
    ) as dialog:
        if dialog.ShowModal() == wx.ID_OK:
            return dialog.GetPath()
    return None


class OpenedFilesDialog(wx.Dialog):
    def __init__(self, parent, entries, current_index=-1):
        super().__init__(
            parent,
            title=_("Opened Files"),
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
        )
        self._entries = list(entries or [])
        self._list = wx.ListBox(self, choices=self._entries)
        if 0 <= current_index < len(self._entries):
            self._list.SetSelection(current_index)

        message = wx.StaticText(self, label=_("Select file to jump to."))
        self._info_button = wx.Button(self, wx.ID_ANY, _("Playlist info"))
        self._jump_button = wx.Button(self, wx.ID_OK, _("Jump to selected"))
        self._cancel_button = wx.Button(self, wx.ID_CANCEL, _("Cancel"))
        self._jump_button.SetDefault()

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(self._info_button, 0, wx.RIGHT, 6)
        button_sizer.AddStretchSpacer(1)
        button_sizer.Add(self._jump_button, 0, wx.RIGHT, 6)
        button_sizer.Add(self._cancel_button, 0)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(message, 0, wx.ALL, 8)
        sizer.Add(self._list, 1, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 8)
        sizer.Add(button_sizer, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 8)
        self.SetSizerAndFit(sizer)
        self.SetMinSize((420, 260))
        self.CentreOnParent()

        self._list.Bind(wx.EVT_LISTBOX_DCLICK, self._on_double_click)

    @property
    def info_button(self):
        return self._info_button

    def get_selection(self):
        return self._list.GetSelection()

    def _on_double_click(self, _event):
        if self.get_selection() != wx.NOT_FOUND:
            self.EndModal(wx.ID_OK)


class TextInfoDialog(wx.Dialog):
    def __init__(self, parent, title, info_text, close_label=None):
        super().__init__(
            parent,
            title=title or _("Information"),
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
        )
        self._text_box = wx.TextCtrl(
            self,
            value=info_text or "",
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_DONTWRAP,
        )
        self._text_box.SetInsertionPoint(0)
        self._text_box.ShowPosition(0)

        close_button = wx.Button(self, wx.ID_CLOSE, close_label or _("Close"))
        close_button.Bind(wx.EVT_BUTTON, self._on_close)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._text_box, 1, wx.ALL | wx.EXPAND, 8)
        sizer.Add(close_button, 0, wx.ALL | wx.ALIGN_RIGHT, 8)
        self.SetSizerAndFit(sizer)
        self.SetMinSize((500, 320))
        self.CentreOnParent()
        self.Bind(wx.EVT_CHAR_HOOK, self._on_char_hook)

    def _on_close(self, _event):
        self.EndModal(wx.ID_CLOSE)

    def _on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
            return
        event.Skip()


class PlaylistInfoDialog(TextInfoDialog):
    def __init__(self, parent, info_text):
        super().__init__(parent, _("Playlist Info"), info_text, close_label=_("Close"))
