# Simple Audio Player - User Guide

## Table of Contents

1. [Getting Started](#getting-started)
2. [Installation & Setup](#installation--setup)
3. [Main Interface](#main-interface)
4. [Basic Playback](#basic-playback)
5. [File Management](#file-management)
6. [Keyboard Shortcuts](#keyboard-shortcuts)
7. [YouTube Features](#youtube-features)
8. [Audio Settings](#audio-settings)
9. [Advanced Features](#advanced-features)
10. [Accessibility & Screen Readers](#accessibility--screen-readers)
11. [Troubleshooting](#troubleshooting)
12. [Frequently Asked Questions](#frequently-asked-questions)

---

## Getting Started

Simple Audio Player is a feature-rich audio and media player designed for Windows with full keyboard accessibility and screen reader support. Whether you're a casual listener or need accessibility features, this guide will help you get the most out of the application.

### What is Simple Audio Player?

Simple Audio Player allows you to:
- Play audio and video files in multiple formats
- Manage large music libraries and playlists
- Search and play YouTube videos
- Process audio with advanced features like silence removal
- Control playback entirely with keyboard shortcuts
- Access all features through screen readers

### System Requirements

- **Operating System:** Windows 7 SP1 or later (Windows 10+ recommended)
- **RAM:** Minimum 256 MB
- **Disk Space:** 200 MB for installation
- **Audio Device:** Working audio output device

---

## Installation & Setup

### Windows Installer (Recommended)

1. Download `SimpleAudioPlayerSetup.exe` from the project releases page
2. Run the installer executable
3. Follow the installation wizard prompts
4. Choose installation directory (default: `%LocalAppData%\Programs\Simple Audio Player`)
5. Select whether to create desktop shortcut
6. Click "Install" and wait for completion
7. Launch the application from Start Menu or desktop shortcut

### Portable Version

1. Download the portable ZIP file
2. Extract to your preferred location
3. Run `SimpleAudioPlayer.exe` directly
4. No installation or elevated permissions required

> **Tip:** Portable version is ideal if you want to use the player from a USB drive or don't have administrator rights on your computer.

### First-Time Setup

When you run Simple Audio Player for the first time:
1. Application window appears with main controls
2. If YouTube features are needed, installation prompt may appear
3. Settings dialog allows customization of preferences
4. Your preferences are automatically saved

---

## Main Interface

### Main Window Layout

The main window contains:
- **Menu Bar:** File, Edit, View, Help menus with dropdown options
- **Control Buttons:** Previous, Rewind, Play/Pause, Forward, Next
- **Status Area:** Displays current file information and playback status

### Menu Structure

| Menu | Options | Purpose |
|------|---------|---------|
| **File** | Open File, Open Folder, Open YouTube Link, YouTube Search, Close File, Close All, Exit | File and application management |
| **Edit** | Copy, Paste, Delete, Rename, Mark Files, Batch Operations | File and playlist editing |
| **Playback** | Play/Pause, Next, Previous, Stop, Shuffle, Repeat | Playback control |
| **Tools** | Audio Devices, Settings, Preferences, Silence Removal | Application settings and tools |
| **Help** | User Guide, Changes, About, Contact Support | Help and information |

---

## Basic Playback

### Opening and Playing Files

1. **Using Menu:** Go to `File → Open File`
2. **Using Keyboard:** Press `Ctrl+O`
3. Select audio or video file from your computer
4. File loads and automatic playback begins (if autoplay enabled)
5. Current file information displayed in status area

### Play and Pause

- **Button:** Click "Play/Pause" button
- **Keyboard:** Press `Space`
- Current playback status announced via text-to-speech
- Press again to resume from same position

### Seeking (Navigation)

| Action | Keyboard Shortcut | Effect |
|--------|-------------------|--------|
| Seek Forward (5 sec) | `Right Arrow` | Skip ahead 5 seconds |
| Seek Backward (5 sec) | `Left Arrow` | Rewind 5 seconds |
| Jump to Start | `Home` | Go to beginning of file |
| Jump to End | `End` | Go to end of file |
| Seek Steps | `Shift+1` through `Shift+0` | Jump by fixed intervals (1s to 60m) |
| Custom Seek Step | `Shift+-` | Jump by your custom seek interval |
| Percent Jumps | `Ctrl+1` through `Ctrl+0` | Jump to 10% through 100% of the file |

> **Tip:** You can also use `Ctrl+Shift+1` through `Ctrl+Shift+0` to jump to 5% offsets (e.g., 15%, 25%, etc.).

> **Note:** Seek steps (Shift+1-0) are fixed presets. Percent jumps (Ctrl+1-0) allow quick navigation through long files.
> You can also use `Ctrl+Shift+1-0` to jump to 5% offsets (e.g., 15%, 25%).

### Volume Control

| Action | Keyboard Shortcut | Effect |
|--------|-------------------|--------|
| Volume Up | `Up Arrow` | Increase volume |
| Volume Down | `Down Arrow` | Decrease volume |
| Maximize Volume | `Shift+Up Arrow` | Set to maximum |
| Mute | `Shift+Down Arrow` | Set to minimum (Mute) |
| Announce Volume | `V` | Current volume spoken aloud |

> **Tip:** Volume control has 1000 steps for fine-grained control. Minimum keyboard increment is 5 steps, but can be set to 1 step in settings.

### Speed Control

| Action | Keyboard Shortcut | Range |
|--------|-------------------|-------|
| Increase Speed | `Ctrl+Up Arrow` | 0.5x to 6.0x |
| Decrease Speed | `Ctrl+Down Arrow` | 0.5x to 6.0x |
| Reset Speed | `Alt+Y` | Return to 1.0x (normal) |
| Announce Speed | `S` | Current speed spoken aloud |

---

## File Management

### Opening Folders

1. Go to `File → Open Folder` or press `Ctrl+Shift+O`
2. Select a folder containing audio files
3. Application scans folder recursively for all audio files
4. Progress dialog shows scanning status
5. All found files added to playlist automatically

> **Note:** Folder scanning looks for all supported audio formats recursively through subfolders. Large folders may take time to scan.

### Navigating Files

| Action | Keyboard Shortcut | Menu Option |
|--------|-------------------|-------------|
| Next File | `Tab` or `Page Down` | Playback → Next |
| Previous File | `Shift+Tab` or `Page Up` | Playback → Previous |
| First File | `Ctrl+Home` | Playback → First |
| Last File | `Ctrl+End` | Playback → Last |
| Go to File | `Ctrl+G` | File → Go to File |
| Open Containing Folder | `Ctrl+F` | File → Open Containing Folder |

### File Operations

#### Rename File
1. Load file or select from playlist
2. Press `Shift+F2` or go to `Edit → Rename`
3. Enter new filename in dialog
4. Press Enter to confirm

#### Delete File
1. Select file to delete
2. Press `Shift+Delete` or go to `Edit → Delete`
3. Confirm deletion in dialog
4. File moved to Recycle Bin

#### File Properties
1. Load file or select from playlist
2. Press `Alt+Enter` or go to `File → File Properties`
3. Standard Windows file properties dialog appears

#### Copy File Path
1. Load file
2. Press `Ctrl+Shift+C` or go to `Edit → Copy`
3. File path copied to clipboard
4. Can be pasted into any text editor

#### Paste Files
1. Copy audio files in Windows Explorer
2. Press `Ctrl+V` in Simple Audio Player
3. Files added to current playlist

### Marking Files (Batch Operations)

Mark files to perform batch operations on multiple files:

#### Marking Operations

| Action | Keyboard Shortcut | Effect |
|--------|-------------------|--------|
| Mark Current File | `Ctrl+K` | Add current file to marked list |
| Mark All Files | `Ctrl+A` | Mark all files in playlist |
| Clear Marks | `Ctrl+Shift+K` | Remove all marks |
| Announce Marked Count | `K` | Speak number of marked files |

#### Batch Operations on Marked Files
- **Copy to Folder:** Copy all marked files to selected directory
- **Move to Folder:** Move all marked files to selected directory
- **Copy to Clipboard:** Copy all marked file paths to clipboard
- **Delete Marked:** Delete all marked files

---

## Keyboard Shortcuts

### Playback Control

| Shortcut | Action |
|----------|--------|
| `Space` or `Enter` | Play / Pause |
| `Tab` or `Page Down` | Next Track |
| `Shift+Tab` or `Page Up` | Previous Track |

### Seeking

| Shortcut | Action |
|----------|--------|
| `Right Arrow` | Seek Forward 5 seconds |
| `Left Arrow` | Seek Backward 5 seconds |
| `Ctrl+Right Arrow` | Seek Forward x2 |
| `Ctrl+Left Arrow` | Seek Backward x2 |
| `Shift+Right Arrow` | Seek Forward x8 |
| `Shift+Left Arrow` | Seek Backward x8 |
| `Ctrl+Shift+Right Arrow` | Seek Forward x4 |
| `Ctrl+Shift+Left Arrow` | Seek Backward x4 |
| `Home` | Jump to Start |
| `End` | Jump to End |
| `Shift+1` through `Shift+9` | Jump by Seek Step 1-9 |
| `Shift+0` | Jump by Seek Step 10 |

### Volume Control

| Shortcut | Action |
|----------|--------|
| `Up Arrow` | Increase Volume |
| `Down Arrow` | Decrease Volume |
| `Shift+Up Arrow` | Maximize Volume |
| `Shift+Down Arrow` | Minimize Volume (Mute) |
| `V` | Announce Volume |

### Speed Control

| Shortcut | Action |
|----------|--------|
| `Ctrl+Up Arrow` | Increase Speed |
| `Ctrl+Down Arrow` | Decrease Speed |
| `Alt+Y` | Reset Speed to 1.0x |
| `S` | Announce Speed |

### File Management

| Shortcut | Action |
|----------|--------|
| `Ctrl+O` | Open File |
| `Ctrl+Shift+O` | Open Folder |
| `Ctrl+W` | Close Current File |
| `Ctrl+Shift+W` | Close All Files |
| `Ctrl+L` | Open Link |
| `F2` | Opened Files List |
| `Shift+F2` | Rename File |
| `Shift+Delete` | Delete File |
| `Ctrl+Shift+C` | Copy File Path |
| `Ctrl+V` | Paste Files |
| `Alt+Enter` | File Properties |

### Navigation

| Shortcut | Action |
|----------|--------|
| `Ctrl+Home` | Go to First File |
| `Ctrl+End` | Go to Last File |
| `Ctrl+G` | Go to Specific File |
| `Ctrl+F` | Open Containing Folder |

### Information

| Shortcut | Action |
|----------|--------|
| `E` | Announce Elapsed Time |
| `R` | Announce Remaining Time |
| `T` | Announce Duration |
| `P` | Announce Current Position % |
| `F` | Announce File Information |

### Marking Files

| Shortcut | Action |
|----------|--------|
| `Ctrl+K` | Mark Current File |
| `Ctrl+A` | Mark All Files |
| `Ctrl+Shift+K` | Clear All Marks |
| `K` | Announce Marked Count |

### Utilities

| Shortcut | Action |
|----------|--------|
| `Ctrl+P` | Open Settings |
| `F1` | Show User Guide |
| `Ctrl+Shift+T` | Test Speakers |
| `Ctrl+Shift+A` | Audio Devices (Sound Cards) |
| `Ctrl+M` | Toggle Silence Removal |
| `Ctrl+Shift+V` | Toggle Verbosity Mode |

> **Tip:** All keyboard shortcuts are customizable. Go to Settings > Keyboard Shortcuts to modify them to your preference.

---

## YouTube Features

### YouTube Search

1. Go to `File → YouTube Search` or press `Ctrl+Y`
2. Enter search query (e.g., "music artist name")
3. Wait for search results to load
4. Select video from results list
5. Video plays immediately

### Opening YouTube Links

1. Copy YouTube video URL to clipboard
2. Go to `File → Open YouTube Link` or press `Ctrl+Shift+Y`
3. Paste URL when prompted
4. Video begins playing automatically

#### Video Actions

| Shortcut | Action |
|----------|--------|
| `Ctrl+D` | Download Video |
| `Alt+D` | Show Video Description |
| `Ctrl+Y` | YouTube Search |

> **Note:** YouTube URLs must start with `https://` and contain valid video ID. URLs like `https://www.youtube.com/watch?v=dQw4w9WgXcQ` are supported.

### Downloading YouTube Videos

1. Search or open YouTube video
2. Go to `Edit → Download Video`
3. Select download options:
   - Video quality (best available to specific resolution)
   - Format (video file, audio only, etc.)
4. Choose save location
5. Download progress displayed in dialog
6. Downloaded file playable offline

### YouTube Components Installation

YouTube features require additional components (yt-dlp):
- Application automatically detects if components are missing
- Installation prompt appears on first YouTube use
- Click "Install" to download and set up components
- Internet connection required for installation

⚠️ **Warning:** Downloading copyrighted YouTube content may violate terms of service. Only download content you have permission to use.

---

## Audio Settings

### Accessing Settings

1. Press `Ctrl+P`, or
2. Go to `Tools → Settings`

### General Settings Tab

- **Language:** Choose English or Arabic
- **Verbosity:** Beginner or Advanced mode
  - Beginner: Less detailed announcements
  - Advanced: Detailed status messages
- **Check for Updates:** Enable/disable automatic update checks

### Audio Device Settings

1. Go to Settings → Audio Device tab
2. View list of available audio devices
3. Select desired output device
4. Settings saved automatically

### Silence Removal Settings

Automatically remove silent sections from audio:

| Setting | Description | Default |
|---------|-------------|---------|
| Enable Silence Removal | Toggle feature on/off | Off |
| Minimum Silence Duration | Silence shorter than this kept (seconds) | 0.5 |
| Silence Threshold | Audio level considered silent (dB) | -30 |
| Detection Mode | Peak or RMS level detection | Peak |

### Audio Normalization

- **Enable Audio Normalization:** Automatically adjusts levels
- **Benefit:** Consistent volume across different audio sources
- **Use Case:** Listening to podcasts or music from various sources

### Mono Conversion

- **Enable Mono Mode:** Convert stereo to single-channel
- **Benefit:** Compatible with single-channel audio devices
- **Use Case:** Using mono headphone or speaker

### Keyboard Shortcuts Customization

1. Go to Settings → Keyboard Shortcuts tab
2. View list of all available actions
3. Select action to customize
4. Press new keyboard shortcut
5. Confirm by clicking Save

⚠️ **Warning:** Some shortcuts (like Alt+F4) are reserved by Windows and cannot be customized.

---

## Advanced Features

### Shuffle and Repeat Modes

| Mode | Behavior | Keyboard |
|------|----------|----------|
| Shuffle | Play files in random order | `Ctrl+Z` |
| Repeat File | Repeat current file continuously | `Ctrl+R` |

### File Selection (Range Selection)

Select ranges of files for batch operations:

| Action | Keyboard Shortcut |
|--------|-------------------|
| Start Selection | `[` |
| End Selection | `]` |
| Clear Selection | `Backspace` |

### Playback Information

Get detailed playback information:
- **Elapsed Time:** Press `T`
- **Remaining Time:** Press `Shift+T`
- **Total Duration:** Press `D`
- **Current Position %:** Press `Ctrl+P`
- **File Information:** Press `F`

### Playlist Information

1. Go to `File → Playlist Information`
2. View:
   - Total number of files
   - Total playlist duration
   - Currently playing file

---

## Accessibility & Screen Readers

### Screen Reader Support

Simple Audio Player works with:
- **JAWS:** Full support for all features
- **NVDA:** Full support for all features
- **Windows Narrator:** Basic support

### Text-to-Speech Output

Many actions provide audio feedback:
- Play/Pause state changes announced
- Volume changes spoken when requested
- File information announced
- Errors and warnings spoken

### Keyboard-Only Operation

Complete application control via keyboard:
- No mouse required for any function
- All menus accessible via Alt key
- Shortcuts available for all common operations

### Beginner vs Advanced Mode

| Mode | Feature | Description |
|------|---------|-------------|
| Beginner | Simple Messages | Only essential feedback provided |
| Advanced | Detailed Messages | Comprehensive status and action information |

> **Tip:** Toggle between modes by pressing `V` when no file is playing.
> **Tip:** Toggle verbosity mode anytime by pressing `Ctrl+Shift+V`.

---

## Troubleshooting

### Common Issues

#### No Sound Output

**Symptoms:** Application runs but no audio plays

**Solutions:**
1. Check Windows audio device is working
2. Verify speakers/headphones are connected
3. Check system volume is not muted
4. Try different audio device in Settings
5. Run "Test Speakers" (Ctrl+Shift+T)
6. Restart application

#### Screen Reader Not Announcing

**Symptoms:** No text-to-speech output from application

**Solutions:**
1. Verify screen reader (JAWS/NVDA) is running
2. Check system volume is not muted
3. Try "Test Speakers" to verify audio output works
4. Restart screen reader
5. Restart application

#### YouTube Search Not Working

**Symptoms:** YouTube features unavailable or searching fails

**Solutions:**
1. Check internet connection
2. Install YouTube components if prompted
3. Update yt-dlp: Go to Tools → Update YouTube Components
4. Verify video URL is valid and public
5. Check if video is region-restricted

#### Application Crashes

**Symptoms:** Application unexpectedly closes

**Solutions:**
1. Disable silence removal in Settings
2. Disable audio normalization
3. Try different audio device
4. Close other applications
5. Reinstall application

#### File Not Playing

**Symptoms:** File selected but won't play

**Solutions:**
1. Verify file is readable and not corrupted
2. Check file format is supported
3. Try different file to confirm format support
4. Convert file to common format (MP3, WAV)

---

## Frequently Asked Questions

### General Questions

**Q: Is Simple Audio Player free?**  
A: Yes, the application is free and open-source.

**Q: Can I use it on Mac or Linux?**  
A: Currently Windows-only. Future cross-platform support is possible.

**Q: Do I need to install anything else?**  
A: YouTube features require yt-dlp components, installed automatically when first used.

### Playback Questions

**Q: What audio formats are supported?**  
A: MP3, FLAC, WAV, OGG, OPUS, AAC, AIFF, ALAC, WMA, and more.

**Q: Can I adjust playback speed?**  
A: Yes, speed adjustable from 0.5x to 6.0x normal speed.

**Q: Does it support playlists?**  
A: Yes, create playlists by opening folders or adding individual files.

### Customization Questions

**Q: Can I customize keyboard shortcuts?**  
A: Yes, all shortcuts customizable in Settings > Keyboard Shortcuts.

**Q: Can I change the language?**  
A: Yes, English and Arabic supported. Change in Settings > General.

**Q: Where are settings saved?**  
A: In the application directory or %LocalAppData% folder depending on installation type.

### YouTube Questions

**Q: Can I download YouTube videos?**  
A: Yes, with restrictions. Only download content you have permission to use.

**Q: What video quality options are available?**  
A: Quality depends on YouTube availability, typically up to 1080p or best available.

### Accessibility Questions

**Q: Does it work with my screen reader?**  
A: Yes, JAWS and NVDA fully supported. Windows Narrator has basic support.

**Q: Can I control everything with keyboard?**  
A: Yes, all features accessible via keyboard with no mouse required.

---

**Simple Audio Player User Guide | Version 1.0.1**  
**Last Updated: February 22, 2026**

For more information, visit the [GitHub Repository](https://github.com/kamalyaser31/simple-player)
