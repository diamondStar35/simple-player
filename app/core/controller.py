import os
import wx

from actions import (
    ACTIONS,
    CHECK_APP_UPDATES,
    ANNOUNCE_DURATION,
    ANNOUNCE_ELAPSED,
    ANNOUNCE_FILE_INFO,
    ANNOUNCE_MARKED_COUNT,
    ANNOUNCE_PERCENT,
    ANNOUNCE_REMAINING,
    ANNOUNCE_SPEED,
    ANNOUNCE_VOLUME,
    CLEAR_SELECTION,
    COPY_CURRENT_FILE,
    DELETE_FILE,
    END_SELECTION,
    GO_TO_FILE,
    GO_FIRST_FILE,
    GO_LAST_FILE,
    MARK_ALL_FILES,
    MARK_CURRENT_FILE,
    CLEAR_MARKED_FILES,
    MARKED_COPY_TO_FOLDER,
    MARKED_MOVE_TO_FOLDER,
    MARKED_COPY_TO_CLIPBOARD,
    MARKED_DELETE,
    NEXT_TRACK,
    OPEN_CONTAINING_FOLDER,
    OPEN_FILE,
    OPEN_LINK,
    OPEN_YOUTUBE_LINK,
    OPEN_YOUTUBE_SEARCH,
    OPEN_USER_GUIDE,
    OPEN_CHANGES,
    OPEN_CONTACT,
    OPEN_ABOUT,
    VIDEO_COPY_LINK,
    VIDEO_DESCRIPTION,
    VIDEO_DOWNLOAD,
    UPDATE_YT_COMPONENTS,
    OPEN_FILE_LIST,
    OPEN_FILE_PROPERTIES,
    OPEN_FOLDER,
    CLOSE_FILE,
    TEST_SPEAKERS,
    OPEN_SETTINGS,
    PLAY_PAUSE,
    PREVIOUS_TRACK,
    RENAME_FILE,
    RESET_SPEED,
    SEEK_BACKWARD,
    SEEK_END,
    SEEK_FORWARD,
    SEEK_START,
    SEEK_STEP_0,
    SEEK_STEP_1,
    SEEK_STEP_2,
    SEEK_STEP_3,
    SEEK_STEP_4,
    SEEK_STEP_5,
    SEEK_STEP_6,
    SEEK_STEP_7,
    SEEK_STEP_8,
    SEEK_STEP_9,
    SEEK_STEP_CUSTOM,
    SOUND_CARDS,
    SPEED_DOWN,
    SPEED_UP,
    START_SELECTION,
    TOGGLE_VERBOSITY,
    TOGGLE_REPEAT_FILE,
    TOGGLE_SILENCE_REMOVAL,
    TOGGLE_SHUFFLE,
    VOLUME_DOWN,
    VOLUME_MAXIMIZE,
    VOLUME_MINIMIZE,
    VOLUME_UP,
    PERCENT_JUMPS,
    PASTE_FROM_CLIPBOARD,
    GLOBAL_SHORTCUT_ACTIONS,
)
from core.action_context import ActionContext
from app_actions.device_actions import open_sound_cards
from app_actions.file_actions import (
    close_file,
    copy_file,
    del_file,
    first_file,
    goto_file,
    last_file,
    next_file,
    open_file,
    open_folder,
    open_props,
    open_here,
    open_link,
    open_list,
    open_paths,
    paste_files,
    prev_file,
    ren_file,
    restore_last,
    say_file,
    spk_test,
)
from app_actions.marked_file_actions import (
    announce_marked_files_count,
    clear_marked_files,
    copy_marked_to_clipboard,
    copy_marked_to_folder,
    delete_marked_files,
    mark_all_files,
    mark_current_file,
    move_marked_to_folder,
)
from app_actions.help_actions import (
    open_guide,
    open_changes,
    open_contact,
    show_about,
)
from core.keyboard_handler import KeyboardHandler
from app_actions.playback_actions import (
    announce_duration,
    announce_elapsed,
    announce_percent,
    announce_remaining,
    announce_speed,
    announce_volume,
    change_speed,
    change_volume,
    clear_selection,
    end_selection,
    jump_to_percent,
    reset_speed,
    seek_end,
    seek_backward,
    seek_forward,
    seek_start,
    set_seek_step,
    set_volume_max,
    set_volume_min,
    start_selection,
    toggle_repeat_file,
    toggle_silence_removal,
    toggle_play_pause,
    toggle_verbosity,
    toggle_shuffle,
)
from core.player import Player
from config.shortcuts import ShortcutManager
from ui.settings_dialog import SettingsDialog
from youtube.actions import (
    copy_link,
    dl_now,
    has_video,
    on_esc,
    open_yt,
    search_yt,
    show_desc,
)
from youtube.startup import install_components_now
from update.actions import (
    check_app_updates_now,
    check_updates_on_startup,
    update_youtube_components_now,
)


class AppController:
    def __init__(self, settings):
        self._settings = settings
        self._player = Player()
        self._ctx = ActionContext(self._player, self._settings)
        self._shortcuts = ShortcutManager(ACTIONS)
        self._global_shortcuts = ShortcutManager(GLOBAL_SHORTCUT_ACTIONS)
        self._global_keyboard = None
        self._action_handlers = {
            PLAY_PAUSE: lambda: toggle_play_pause(self._ctx),
            SEEK_BACKWARD: lambda: seek_backward(self._ctx),
            SEEK_FORWARD: lambda: seek_forward(self._ctx),
            SEEK_START: lambda: seek_start(self._ctx),
            SEEK_END: lambda: seek_end(self._ctx),
            VOLUME_UP: lambda: change_volume(self._ctx, self._settings.get_volume_step()),
            VOLUME_DOWN: lambda: change_volume(self._ctx, -self._settings.get_volume_step()),
            VOLUME_MAXIMIZE: lambda: set_volume_max(self._ctx),
            VOLUME_MINIMIZE: lambda: set_volume_min(self._ctx),
            ANNOUNCE_VOLUME: lambda: announce_volume(self._ctx),
            ANNOUNCE_ELAPSED: lambda: announce_elapsed(self._ctx),
            ANNOUNCE_REMAINING: lambda: announce_remaining(self._ctx),
            ANNOUNCE_DURATION: lambda: announce_duration(self._ctx),
            ANNOUNCE_PERCENT: lambda: announce_percent(self._ctx),
            ANNOUNCE_SPEED: lambda: announce_speed(self._ctx),
            TOGGLE_VERBOSITY: lambda: toggle_verbosity(self._ctx),
            RESET_SPEED: lambda: reset_speed(self._ctx),
            OPEN_FILE: lambda: open_file(self._ctx),
            OPEN_LINK: lambda: open_link(self._ctx),
            OPEN_YOUTUBE_LINK: lambda: open_yt(self._ctx),
            OPEN_YOUTUBE_SEARCH: lambda: search_yt(self._ctx),
            VIDEO_DOWNLOAD: lambda: dl_now(self._ctx),
            VIDEO_DESCRIPTION: lambda: show_desc(self._ctx),
            VIDEO_COPY_LINK: lambda: copy_link(self._ctx),
            OPEN_USER_GUIDE: lambda: open_guide(self._ctx),
            OPEN_CHANGES: lambda: open_changes(self._ctx),
            OPEN_CONTACT: lambda: open_contact(self._ctx),
            OPEN_ABOUT: lambda: show_about(self._ctx),
            CHECK_APP_UPDATES: lambda: check_app_updates_now(self._ctx),
            UPDATE_YT_COMPONENTS: lambda: update_youtube_components_now(self._ctx),
            OPEN_FOLDER: lambda: open_folder(self._ctx),
            OPEN_CONTAINING_FOLDER: lambda: open_here(self._ctx),
            OPEN_FILE_PROPERTIES: lambda: open_props(self._ctx),
            OPEN_FILE_LIST: lambda: open_list(self._ctx),
            CLOSE_FILE: lambda: close_file(self._ctx),
            TEST_SPEAKERS: lambda: spk_test(self._ctx),
            OPEN_SETTINGS: self.open_settings_dialog,
            GO_TO_FILE: lambda: goto_file(self._ctx),
            GO_FIRST_FILE: lambda: first_file(self._ctx),
            GO_LAST_FILE: lambda: last_file(self._ctx),
            NEXT_TRACK: lambda: next_file(self._ctx),
            PREVIOUS_TRACK: lambda: prev_file(self._ctx),
            DELETE_FILE: lambda: del_file(self._ctx),
            RENAME_FILE: lambda: ren_file(self._ctx),
            COPY_CURRENT_FILE: lambda: copy_file(self._ctx),
            PASTE_FROM_CLIPBOARD: lambda: paste_files(self._ctx),
            MARK_CURRENT_FILE: lambda: mark_current_file(self._ctx),
            ANNOUNCE_MARKED_COUNT: lambda: announce_marked_files_count(self._ctx),
            MARK_ALL_FILES: lambda: mark_all_files(self._ctx),
            CLEAR_MARKED_FILES: lambda: clear_marked_files(self._ctx),
            MARKED_COPY_TO_FOLDER: lambda: copy_marked_to_folder(self._ctx),
            MARKED_MOVE_TO_FOLDER: lambda: move_marked_to_folder(self._ctx),
            MARKED_COPY_TO_CLIPBOARD: lambda: copy_marked_to_clipboard(self._ctx),
            MARKED_DELETE: lambda: delete_marked_files(self._ctx),
            ANNOUNCE_FILE_INFO: lambda: say_file(self._ctx),
            START_SELECTION: lambda: start_selection(self._ctx),
            END_SELECTION: lambda: end_selection(self._ctx),
            CLEAR_SELECTION: lambda: clear_selection(self._ctx),
            SEEK_STEP_1: lambda: set_seek_step(self._ctx, "1"),
            SEEK_STEP_2: lambda: set_seek_step(self._ctx, "2"),
            SEEK_STEP_3: lambda: set_seek_step(self._ctx, "3"),
            SEEK_STEP_4: lambda: set_seek_step(self._ctx, "4"),
            SEEK_STEP_5: lambda: set_seek_step(self._ctx, "5"),
            SEEK_STEP_6: lambda: set_seek_step(self._ctx, "6"),
            SEEK_STEP_7: lambda: set_seek_step(self._ctx, "7"),
            SEEK_STEP_8: lambda: set_seek_step(self._ctx, "8"),
            SEEK_STEP_9: lambda: set_seek_step(self._ctx, "9"),
            SEEK_STEP_0: lambda: set_seek_step(self._ctx, "0"),
            SEEK_STEP_CUSTOM: lambda: set_seek_step(self._ctx, "-"),
            SPEED_UP: lambda: change_speed(self._ctx, self._settings.get_speed_step()),
            SPEED_DOWN: lambda: change_speed(self._ctx, -self._settings.get_speed_step()),
            SOUND_CARDS: lambda: open_sound_cards(self._ctx),
            TOGGLE_SHUFFLE: lambda: toggle_shuffle(self._ctx),
            TOGGLE_REPEAT_FILE: lambda: toggle_repeat_file(self._ctx),
            TOGGLE_SILENCE_REMOVAL: lambda: toggle_silence_removal(self._ctx),
        }
        for action_id, percent in PERCENT_JUMPS.items():
            self._action_handlers[action_id] = (
                lambda percent=percent: jump_to_percent(self._ctx, percent)
            )
        self._load_shortcuts_from_settings()
        self._player.set_volume(self._settings.get_volume())
        self._player.set_speed(self._settings.get_speed())
        self._player.set_end_behavior(self._settings.get_end_behavior())
        device = self._settings.get_audio_device()
        if device:
            self._player.set_audio_device(device)
        self._player.set_audio_normalize_enabled(
            self._settings.get_audio_normalize_enabled()
        )
        self._player.set_audio_mono_enabled(
            self._settings.get_audio_mono_enabled()
        )
        self._player.configure_silence_removal(
            self._settings.get_silence_removal_options()
        )
        self._player.set_silence_removal_enabled(
            self._settings.get_silence_removal_enabled()
        )

    def attach_frame(self, frame):
        self._ctx.set_frame(frame)
        video_handle = frame.get_video_window_handle()
        self._player.set_render_window(video_handle)
        self._ensure_global_shortcuts_started()
        self._ctx.set_file_loaded(False)
        self._sync_frame_toggles()

    def get_shortcuts(self):
        return self._shortcuts.all_shortcuts()

    def get_shortcut_bindings(self):
        return self._shortcuts.all_bindings()

    def open_settings_dialog(self):
        if self._ctx.frame is None:
            return
        old_lang = self._settings.get_ui_language()
        dialog = SettingsDialog(
            self._ctx.frame,
            self._settings,
            on_download_youtube_components=self._download_yt_components,
        )
        if dialog.ShowModal() == wx.ID_OK:
            dialog.apply()
            self._settings.save()
            self._load_shortcuts_from_settings()
            if self._ctx.frame is not None:
                self._ctx.frame.refresh_shortcuts()
            self._player.set_end_behavior(self._settings.get_end_behavior())
            self._player.set_audio_normalize_enabled(
                self._settings.get_audio_normalize_enabled()
            )
            self._player.set_audio_mono_enabled(
                self._settings.get_audio_mono_enabled()
            )
            self._player.configure_silence_removal(
                self._settings.get_silence_removal_options()
            )
            self._player.set_silence_removal_enabled(
                self._settings.get_silence_removal_enabled()
            )
            new_lang = self._settings.get_ui_language()
            if str(new_lang or "") != str(old_lang or ""):
                wx.MessageBox(
                    _("Please restart the app for language changes to take effect."),
                    _("Preferences"),
                    wx.OK | wx.ICON_INFORMATION,
                    parent=self._ctx.frame,
                )
        dialog.Destroy()

    def restore_last_session(self):
        restore_last(self._ctx)
        self._sync_frame_toggles()

    def run_startup_tasks(self):
        return bool(check_updates_on_startup(self._ctx))

    def open_paths_from_shell(self, raw_paths):
        if open_paths(self._ctx, raw_paths):
            self._sync_frame_toggles()
            return True
        return False

    def shutdown(self):
        try:
            if self._global_keyboard is not None:
                self._global_keyboard.stop()
                self._global_keyboard = None
            self._settings.set_volume(self._player.get_volume())
            self._settings.set_speed(self._player.get_speed())
            if self._settings.get_remember_position():
                path = self._player.current_path
                position = self._player.get_elapsed()
                if path and position is not None and os.path.isfile(path):
                    self._settings.set_last_file_position(path, position)
            self._settings.save()
        finally:
            self._player.shutdown()

    def handle_action(self, action_id):
        handler = self._action_handlers.get(action_id)
        if handler is None:
            return
        wx.CallAfter(self._run_action_and_sync, handler)

    def handle_escape(self):
        return bool(on_esc(self._ctx))

    def _download_yt_components(self, parent, channel):
        install_components_now(parent, self._settings, channel=channel)

    def _run_action_and_sync(self, handler):
        handler()
        self._sync_frame_toggles()

    def _sync_frame_toggles(self):
        frame = self._ctx.frame
        if frame is None:
            return
        frame.set_shuffle_checked(self._player.is_shuffle_enabled())
        frame.set_repeat_file_checked(self._player.is_repeat_file_enabled())
        frame.set_silence_removal_checked(self._player.is_silence_removal_enabled())
        frame.set_mark_current_checked(self._player.is_current_marked())
        frame.set_mark_all_checked(self._player.are_all_files_marked())
        frame.set_marked_actions_enabled(self._player.has_marked_files())
        is_local = os.path.isfile(self._player.current_path or "")
        frame.set_file_properties_enabled(is_local)
        frame.set_local_file_actions_enabled(is_local)
        frame.set_video_options_enabled(has_video(self._ctx))

    def _load_shortcuts_from_settings(self):
        self._shortcuts = ShortcutManager(ACTIONS)
        for action_id, shortcut in self._settings.get_shortcut_overrides().items():
            self._shortcuts.set(action_id, shortcut)
        for action_id, shortcut in self._settings.get_secondary_shortcut_overrides().items():
            self._shortcuts.set(action_id, shortcut, slot="secondary")

        self._global_shortcuts = ShortcutManager(GLOBAL_SHORTCUT_ACTIONS)
        for action_id, shortcut in self._settings.get_global_shortcut_overrides().items():
            self._global_shortcuts.set(action_id, shortcut)

        if self._global_keyboard is not None:
            self._global_keyboard.set_shortcuts(self._global_shortcuts.all_bindings())

    def _ensure_global_shortcuts_started(self):
        if self._global_keyboard is not None:
            self._global_keyboard.set_shortcuts(self._global_shortcuts.all_bindings())
            return
        self._global_keyboard = KeyboardHandler(
            self._global_shortcuts.all_bindings(),
            self._on_global_action,
        )
        self._global_keyboard.start()

    def _on_global_action(self, action_id):
        self.handle_action(action_id)

