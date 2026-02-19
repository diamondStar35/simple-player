import os

from config.constants import AUDIO_EXTENSIONS


def collect_audio_files(folder_path, recursive=False):
    entries = []
    try:
        if recursive:
            for root, _dirs, files in os.walk(folder_path):
                for name in files:
                    _, ext = os.path.splitext(name)
                    if ext.lower() in AUDIO_EXTENSIONS:
                        entries.append(os.path.join(root, name))
        else:
            for name in os.listdir(folder_path):
                full = os.path.join(folder_path, name)
                if not os.path.isfile(full):
                    continue
                _, ext = os.path.splitext(name)
                if ext.lower() in AUDIO_EXTENSIONS:
                    entries.append(full)
    except OSError:
        return []

    if recursive:
        entries.sort(key=lambda p: p.lower())
    else:
        entries.sort(key=lambda p: os.path.basename(p).lower())
    return entries

