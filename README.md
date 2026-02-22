# Simple Audio Player

A feature-rich, accessible Windows desktop audio and media player built with Python and wxPython. Designed with keyboard accessibility and screen reader support in mind.

**Version:** 1.0.1  
**Author:** Kamal Yaser  
**Repository:** [GitHub](https://github.com/kamalyaser31/simple-player)

---

## Table of Contents

- [Features](#features)
- [Supported Formats](#supported-formats)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Configuration](#configuration)
- [YouTube Features](#youtube-features)
- [Audio Processing](#audio-processing)
- [Troubleshooting](#troubleshooting)
- [Development](#development)
- [License](#license)
- [Support](#support)

---

## Features

### Core Playback
- **Multiple Format Support:** Play audio and video files in 20+ formats
- **Playback Controls:** Play/Pause, Next, Previous, Stop, Seek operations
- **Variable Speed Playback:** Adjust playback speed from 0.5x to 6.0x normal speed
- **Volume Control:** Granular volume control with 1000 steps (5-step increments minimum)
- **Shuffle Mode:** Randomized playback order with automatic file cycling

### Playlist & File Management
- **Smart File Browsing:** Navigate files with next/previous/first/last controls
- **Folder Operations:** Open folders and recursively scan for audio files
- **File Actions:** Rename, delete, copy files directly from the player
- **Clipboard Integration:** Copy/paste files to clipboard for quick access
- **File Marking:** Mark files for batch operations
- **Recently Opened:** Quickly restore and continue playing previously opened files
- **Playlist Info:** View detailed information about loaded files and total duration

### YouTube Integration
- **YouTube Video Search:** Search and play YouTube videos directly
- **Video Download:** Download YouTube videos and playlists to local storage
- **Link Validation:** Automatic detection and parsing of YouTube URLs
- **Playlist Support:** Handle YouTube playlists with individual video selection
- **Auto-Update:** Automatically fetch the latest yt-dlp binaries for compatibility

### Audio Processing
- **Silence Removal:** Intelligent silence detection and trimming with customizable parameters:
  - Minimum silence duration threshold
  - Configurable detection sensitivity levels
  - Advanced start/stop silence period configuration
  - Smoothing window adjustment for fine-tuning
- **Audio Normalization:** Volume normalization across different audio sources
- **Mono Conversion:** Convert stereo audio to mono playback
- **Audio Preamp:** Adjust audio preamplification for volume optimization

### Accessibility
- **Screen Reader Support:** Full integration with accessible_output3
- **Text-to-Speech:** Audio feedback for all player actions and status updates
- **Beginner/Advanced Modes:** Adjustable verbosity levels for user feedback
- **Keyboard-Only Operation:** Complete functionality accessible via keyboard
- **Global Hotkeys:** Use keyboard shortcuts even when window is unfocused

### Customization
- **Configurable Shortcuts:** Customize all keyboard shortcuts to your preference
- **Audio Device Selection:** Choose between available sound cards
- **Multi-Language Support:** English and Arabic language options
- **Settings Persistence:** All preferences saved automatically
- **Theme Support:** Accessible UI design compatible with system themes

### System Integration
- **File Associations:** Automatically register audio/video formats with Windows
- **Context Menu Integration:** "Play with Simple Audio Player" option in Windows Explorer
- **Single Instance Mode:** Only one application instance runs at a time
- **Windows Media Session:** Integration with Windows media controls
- **Auto-Update System:** Check for and download application updates

---

## Supported Formats

### Audio Formats
- AAC, AIFF, ALAC, FLAC, M4A, MP3, OGG, OPUS, WAV, WMA

### Video Formats
- 3GP, AVI, FLV, M2TS, M4V, MKV, MOV, MPEG, MP4, MPG, TS, WebM, WMV

---

## System Requirements

### Minimum Requirements
- **OS:** Windows 7 SP1 or later (Windows 10+ recommended)
- **Architecture:** 32-bit or 64-bit
- **RAM:** 256 MB minimum
- **Disk Space:** 200 MB for installation

### Dependencies
- **Python 3.7+** (for development/source installation)
- **wxPython:** GUI framework
- **python-libmpv:** Media playback engine
- **pynput:** Global keyboard input handling
- **accessible_output3:** Screen reader integration
- **py-yt-search:** YouTube search functionality
- **winsdk:** Windows SDK integration

---

## Installation

### Option 1: Windows Installer (Recommended)

1. Download the latest installer from the [Releases page](https://github.com/kamalyaser31/simple-player/releases)
2. Run `SimpleAudioPlayerSetup.exe`
3. Follow the installation wizard
4. Choose installation directory (default: `%LocalAppData%\Programs\Simple Audio Player`)
5. Optionally create a desktop shortcut
6. Launch the application

### Option 2: Portable ZIP Version

1. Download the portable ZIP file from the [Releases page](https://github.com/kamalyaser31/simple-player/releases)
2. Extract to your preferred location
3. Run `SimpleAudioPlayer.exe`

### Option 3: Installation from Source

#### Prerequisites
- Python 3.7 or higher
- Git
- Visual C++ Build Tools (for compiling dependencies)

#### Steps

1. **Clone the Repository**
   ```powershell
   git clone https://github.com/kamalyaser31/simple-player.git
   cd simple-player/player
   ```

2. **Create Virtual Environment (Optional but Recommended)**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```powershell
   python SimpleAudioPlayer.py
   ```

#### Building an Executable

1. **Install PyInstaller**
   ```powershell
   pip install pyinstaller
   ```

2. **Build the Executable**
   ```powershell
   pyinstaller SimpleAudioPlayer.spec
   ```

3. **Find Output**
   - Executable located in `dist/SimpleAudioPlayer/SimpleAudioPlayer.exe`

#### Building Windows Installer

1. **Install Inno Setup** from [jrsoftware.org](https://jrsoftware.org/isdl.php)

2. **Build Executable First** (see above)

3. **Run Inno Setup Compiler**
   ```powershell
   "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" simple_audio_player.iss
   ```

4. **Find Installer**
   - Installer located in `dist/SimpleAudioPlayerSetup.exe`

---

## Usage

### Basic Operation

1. **Open File:** `File > Open File` or use keyboard shortcut
   - Supports single files, entire folders, and drag-and-drop

2. **Play/Pause:** Press spacebar or click Play button
   - Current playback status announced via text-to-speech

3. **Navigate Files:** Use Next/Previous controls or keyboard shortcuts
   - Automatic progression through playlist or manual navigation

4. **Adjust Volume:** Use Volume Up/Down keys or slider
   - Current volume percentage announced

5. **Seek in File:** Use Seek Forward/Backward controls or predefined intervals
   - Elapsed and remaining time available on demand

### Advanced Features

**Folder Scanning:**
- Open a folder to load all audio files recursively
- Progress dialog shows scanning status
- Hierarchical folder structure preserved in playlist

**YouTube Playback:**
- Open YouTube video URLs directly
- Search for videos using the YouTube search feature
- Download videos for offline playback

**File Marking:**
- Mark current file or all files in playlist
- Perform batch operations (copy, move, delete) on marked files

**Audio Processing:**
- Enable silence removal in settings for automatic silence trimming
- Configure normalization and mono conversion as needed
- Adjust preamp settings for volume optimization

---

## Keyboard Shortcuts

### Playback Control
| Action | Shortcut |
|--------|----------|
| Play/Pause | `Space` |
| Next Track | `Ctrl+Right` or `N` |
| Previous Track | `Ctrl+Left` or `P` |
| Seek Forward (5s) | `Right Arrow` |
| Seek Backward (5s) | `Left Arrow` |
| Seek to Start | `Home` |
| Seek to End | `End` |

### Volume Control
| Action | Shortcut |
|--------|----------|
| Volume Up | `Ctrl+Up` or `+` |
| Volume Down | `Ctrl+Down` or `-` |
| Mute/Maximize Volume | `M` |
| Announce Volume | `V` |

### File Operations
| Action | Shortcut |
|--------|----------|
| Open File | `Ctrl+O` |
| Open Folder | `Ctrl+Shift+O` |
| Open YouTube Link | `Ctrl+Y` |
| Close Current File | `Ctrl+W` |
| Close All Files | `Ctrl+Shift+W` |
| Copy File Path | `Ctrl+C` |
| Rename File | `F2` |
| Delete File | `Delete` |

### Navigation
| Action | Shortcut |
|--------|----------|
| Go to First File | `Ctrl+Home` |
| Go to Last File | `Ctrl+End` |
| Go to File by Index | `Ctrl+G` |

### Information
| Action | Shortcut |
|--------|----------|
| Announce Time Elapsed | `T` |
| Announce Time Remaining | `Shift+T` |
| Announce Current Position % | `Ctrl+P` |
| Announce File Info | `F` |

### Utilities
| Action | Shortcut |
|--------|----------|
| Open Settings | `Ctrl+Comma` |
| Toggle Verbosity Mode | `V` (when no file playing) |
| Test Speakers | `Ctrl+Alt+T` |
| Show User Guide | `F1` |

**Note:** All shortcuts are customizable via Settings > Keyboard Shortcuts

---

## Configuration

### Settings File Location
- **Installed Version:** `%LocalAppData%\Simple Audio Player\settings.ini`
- **Portable Version:** `settings.ini` in the application directory

### Configuration Options

#### General Settings
- **UI Language:** English or Arabic
- **Verbosity Level:** Beginner or Advanced mode
- **Auto-Update Check:** Enable/disable automatic update checks

#### Audio Device
- **Output Device:** Select default audio device or specific sound card
- **Audio Driver:** Automatically detected from available devices

#### Playback Preferences
- **Default Volume:** Set initial volume level
- **Repeat Mode:** File or playlist repeat options
- **Shuffle Default:** Enable/disable shuffle on startup

#### Audio Processing
- **Silence Removal:** Enable/disable automatic silence trimming
  - Minimum silence duration
  - Detection threshold level
  - Detection mode (peak or RMS)
  - Advanced parameters for fine control
- **Audio Normalization:** Enable loudness normalization
- **Mono Conversion:** Convert stereo to mono

#### YouTube Settings
- **yt-dlp Channel:** Select update channel (stable, nightly, or master)
- **Video Quality:** Preferred video quality for downloads
- **Audio-Only:** Download audio tracks only

#### Keyboard Shortcuts
- Customize all keyboard shortcuts
- Set primary and secondary shortcuts for common actions
- Export/import shortcut configurations

---

## YouTube Features

### Searching and Playing
1. Go to `File > YouTube Search` or press `Ctrl+Y`
2. Enter search query or YouTube URL
3. Select video from results
4. Video plays immediately upon selection

### Downloading Videos
1. Open YouTube video URL or search for video
2. Right-click video in results
3. Select "Download Video"
4. Choose quality and audio settings
5. Download progress displayed in dialog

### Handling Playlists
- If URL contains both playlist and video IDs, choose how to proceed:
  - Play entire playlist
  - Play specific video only

### Components Installation
- YouTube features require yt-dlp binaries
- Application automatically detects missing components
- One-click installation available from settings or startup prompt

---

## Audio Processing

### Silence Removal
Removes silent portions from audio tracks automatically:

**Basic Settings:**
- **Enabled:** Toggle silence removal on/off
- **Minimum Duration:** Silence shorter than this kept (default: 0.5s)
- **Threshold:** Audio level threshold for silence detection (default: -30dB)
- **Detection Mode:** Peak or RMS level detection (default: peak)

**Advanced Settings:**
- **Leading Silence Removal:** Remove N leading silent chunks
- **Inner Silence Removal:** Remove N silence chunks after audio starts
- **Silence Padding:** Keep brief pause after removed silence

### Audio Normalization
Automatically adjusts audio levels for consistent loudness:
- Uses dynamic audio normalization filter
- Prevents volume spikes between tracks
- Smooths out wide dynamic range

### Mono Conversion
Converts stereo audio to single-channel mono playback:
- Useful for single-channel audio devices
- Reduces file processing load
- Maintains audio quality

---

## Troubleshooting

### Application Won't Start
**Problem:** Application fails to launch  
**Solution:**
- Verify Windows version compatibility (Windows 7 SP1+)
- Reinstall from installer or source
- Check antivirus/firewall blocking

### No Sound Output
**Problem:** Application launches but no audio plays  
**Solution:**
- Verify audio device selection in settings
- Check Windows audio output device is working
- Try different audio device in settings
- Test speakers using `Test Speakers` button

### Screen Reader Not Working
**Problem:** Text-to-speech feedback not heard  
**Solution:**
- Verify screen reader is running (JAWS, NVDA, etc.)
- Check system volume is not muted
- Verify accessible_output3 library is installed
- Restart application after screen reader starts

### YouTube Features Not Working
**Problem:** YouTube search/download features unavailable  
**Solution:**
- Install missing YouTube components when prompted
- Check internet connection
- Verify yt-dlp is up to date (auto-update available)
- Check if video/URL is region-restricted

### File Association Issues
**Problem:** Audio files don't open with Simple Audio Player  
**Solution:**
- Re-register file associations via Settings
- Use Windows "Open With" menu to select application
- Manually select file in player's Open dialog

### Performance Issues
**Problem:** Application laggy or audio stutters  
**Solution:**
- Disable silence removal if not needed
- Disable audio normalization if not needed
- Close other background applications
- Check disk space availability
- Update audio drivers

### Settings Not Saving
**Problem:** Settings revert after restart  
**Solution:**
- Verify write permissions to settings directory
- Check antivirus not blocking file writes
- Delete corrupted settings.ini and recreate
- Run installer repair function

---

## Development

### Project Structure

```
simple-player/
├── player/                    # Main application directory
│   ├── app.py                # Application entry point
│   ├── SimpleAudioPlayer.py   # GUI entry point
│   ├── requirements.txt       # Python dependencies
│   ├── SimpleAudioPlayer.spec # PyInstaller configuration
│   ├── simple_audio_player.iss # Inno Setup configuration
│   │
│   ├── core/                 # Core functionality
│   │   ├── controller.py     # Main application controller
│   │   ├── mpv_engine.py     # Media playback engine
│   │   ├── keyboard_handler.py # Global keyboard input
│   │   ├── media_library.py  # File scanning/indexing
│   │   └── player/           # Player implementation
│   │
│   ├── config/               # Configuration management
│   │   ├── constants.py      # Application constants
│   │   ├── settings_manager.py # Settings persistence
│   │   ├── shortcuts.py      # Keyboard shortcuts
│   │   ├── localization.py   # i18n support
│   │   └── file_associations.py # Windows file registration
│   │
│   ├── ui/                   # User interface
│   │   ├── main_frame.py     # Main window
│   │   ├── mainwin/          # Main window components
│   │   ├── dialogs.py        # UI dialogs
│   │   ├── settings_dialog.py # Settings window
│   │   └── prefs/            # Settings panels
│   │
│   ├── app_actions/          # Application actions
│   │   ├── playback_actions.py # Playback control
│   │   ├── file_actions.py   # File operations
│   │   ├── device_actions.py # Audio device management
│   │   └── help_actions.py   # Help/documentation
│   │
│   ├── youtube/              # YouTube integration
│   │   ├── search.py         # Search functionality
│   │   ├── download.py       # Download functionality
│   │   ├── flow.py           # YouTube workflow
│   │   └── components.py     # Component management
│   │
│   ├── playlist/             # Playlist management
│   │   ├── state.py          # Playlist state
│   │   └── state/            # Playlist state modules
│   │
│   ├── helpers/              # Utility functions
│   │   ├── utils.py          # Common utilities
│   │   ├── file_helpers.py   # File operations
│   │   └── clipboard_utils.py # Clipboard handling
│   │
│   ├── locale/               # Localization files
│   │   └── ar/, en/          # Language directories
│   │
│   ├── docs/                 # Documentation
│   │   └── en/, ar/          # Language docs
│   │
│   └── sounds/               # Audio resources
│       └── speaker_test.wav  # Test sound file
```

### Dependencies

| Package | Purpose |
|---------|---------|
| `wxPython` | GUI framework |
| `python-libmpv` | Media playback |
| `pynput` | Global keyboard handling |
| `appGuard` | Single instance enforcement |
| `accessible_output3` | Screen reader integration |
| `py-yt-search` | YouTube search |
| `winsdk` | Windows SDK integration |

### Building from Source

#### Development Setup
```powershell
# Clone repository
git clone https://github.com/kamalyaser31/simple-player.git
cd simple-player/player

# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run application
python SimpleAudioPlayer.py
```

#### Running Tests
```powershell
# Run syntax check
python -m py_compile *.py
python -m py_compile app_actions/*.py
python -m py_compile core/*.py
# ... repeat for all directories
```

#### Building Executable
```powershell
pip install pyinstaller

# Build one-file executable
pyinstaller SimpleAudioPlayer.spec

# Output: dist/SimpleAudioPlayer/SimpleAudioPlayer.exe
```

#### Creating Installer
```powershell
# Install Inno Setup from jrsoftware.org

# Build executable first
pyinstaller SimpleAudioPlayer.spec

# Create installer
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" simple_audio_player.iss

# Output: dist/SimpleAudioPlayerSetup.exe
```

### Code Organization

**Action System:**
- All user actions defined in `actions.py`
- Action handlers in `app_actions/` directory
- Actions dispatched through `core/controller.py`

**State Management:**
- Player state in `core/player/state.py`
- Playlist state in `playlist/state/`
- Settings state in `config/settings_manager.py`

**UI Components:**
- Main window in `ui/main_frame.py`
- Dialogs in `ui/dialogs.py`
- Settings panels in `ui/prefs/`

**Localization:**
- Translation strings marked with `_()` function
- POT template in `locale/simple_audio_player.pot`
- Language-specific translations in `locale/[lang]/LC_MESSAGES/`

### Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## License

This project is licensed under the MIT License. See LICENSE file for details.

---

## Support

### Getting Help

- **User Guide:** Available in application at `Help > User Guide`
- **Report Issues:** [GitHub Issues](https://github.com/kamalyaser31/simple-player/issues)
- **Email Support:** kamalyaser31@gmail.com
- **Telegram:** [@kamalyaser31](https://t.me/kamalyaser31)

### Feedback and Suggestions

Your feedback is valuable! Please report issues or suggest improvements through:
- GitHub Issues tracker
- Email
- Telegram channel

### Frequently Asked Questions

**Q: Is the application portable?**  
A: Yes! Both portable ZIP and installer versions available.

**Q: Does it work on Linux/Mac?**  
A: Currently Windows-only. Potential cross-platform support in future.

**Q: Can I customize keyboard shortcuts?**  
A: Yes! Full customization available in Settings > Keyboard Shortcuts.

**Q: Is internet connection required?**  
A: No for local files. Required only for YouTube features and auto-updates.

**Q: How do I uninstall?**  
A: Use Windows "Programs and Features" to uninstall, or delete portable folder.

---

## Changelog

### Version 1.0.1
- Stability improvements
- Enhanced YouTube integration
- Improved accessibility features

### Version 1.0.0
- Initial release
- Core playback functionality
- YouTube integration
- Advanced audio processing
- Multi-language support

---

## Project Statistics

- **Languages Used:** Python (primary), HTML (docs)
- **Lines of Code:** ~10,000+
- **Supported Languages:** English, Arabic
- **Supported Audio Formats:** 10+
- **Supported Video Formats:** 13+
- **Total Keyboard Actions:** 80+
- **Platform:** Windows 7 SP1+

---

**Last Updated:** February 22, 2026  
**Project Version:** 1.0.1

For the latest updates and releases, visit the [GitHub Repository](https://github.com/kamalyaser31/simple-player).
