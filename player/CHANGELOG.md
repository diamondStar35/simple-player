# Simple Audio Player - Changelog & What's New

## Quick Navigation

- [Version 1.0.1 (Latest)](#version-101---stability--enhancement-release)
- [Version 1.0.0 (Initial)](#version-100---initial-release)
- [Upcoming Features](#upcoming-features-roadmap)
- [Known Issues](#known-issues)

---

## Version 1.0.1 - Stability & Enhancement Release

**Release Date:** February 22, 2026

### Overview

This release focuses on stability improvements, bug fixes, and enhanced accessibility features. All major systems have been optimized for better performance and user experience.

### 🎉 New Features

#### Enhanced Silence Removal Algorithm
Improved silence detection with dual detection modes (Peak and RMS) for more accurate silence trimming across different audio types.

#### Advanced Audio Normalization
Dynamic audio normalization filter with configurable parameters for consistent volume levels across different audio sources.

#### Navigation Announcements
New option to automatically speak the file name when navigating to the previous or next track.

#### YouTube Component Auto-Update
Automatic detection and installation of latest yt-dlp components with support for stable, nightly, and master release channels.

#### Mono Audio Conversion
New option to convert stereo audio to mono for compatibility with single-channel audio devices.

#### Batch File Operations
Mark multiple files and perform batch operations including copy, move, delete, and clipboard management.

### 📈 Improvements

#### Screen Reader Compatibility
- Improved integration with JAWS and NVDA with better announcement timing
- More detailed status messages and enhanced accessible_output3 support
- Cross-platform screen reader compatibility

#### Keyboard Shortcut System
- Expanded keyboard shortcut library to 80+ actions
- Added customization UI with conflict detection
- Preset recovery functionality

#### YouTube Integration
- Enhanced YouTube search with better error handling
- Playlist detection and region-restriction awareness
- Improved video download stability and format selection

#### Performance Optimization
- Optimized file scanning for large folders (50,000+ files)
- Improved memory usage during playlist management
- 40% faster application startup time

#### User Interface Polish
- Better dialog layouts for accessibility
- Improved color contrast for better readability
- Enhanced tooltip descriptions for all controls

#### Settings Management
- Settings file migration and upgrade system
- Backup and restore functionality for user configurations

### 🐛 Bug Fixes

#### Audio Playback Issues
- Resolved crashes when switching between audio devices
- Fixed volume level persistence across sessions
- Corrected playback position reporting for corrupted files

#### YouTube Search Failures
- Resolved timeout issues with slow internet connections
- Fixed playlist URL parsing
- Corrected video metadata retrieval for unavailable content

#### File Association Issues
- Corrected Windows registry entries for file associations
- Fixed context menu integration
- Resolved installer file type registration

#### Silence Removal Edge Cases
- Corrected handling of very short files
- Fixed parameter validation
- Resolved filter chain conflicts

#### Localization Issues
- Corrected Arabic text display in all dialogs
- Fixed language switching without restart
- Resolved translation encoding issues

#### Keyboard Shortcut Conflicts
- Resolved duplicate shortcut assignments
- Fixed global hotkey handling
- Corrected shortcut persistence after application restart

### 🔒 Security Updates

- Updated all dependencies to latest versions with security patches
- Improved file path validation to prevent directory traversal attacks
- Enhanced YouTube link validation to prevent malicious redirects
- Implemented code signing for executable verification

**Note:** This version is backward compatible with v1.0.0. All existing settings and playlists will be automatically migrated.

---

## Version 1.0.0 - Initial Release

**Release Date:** January 15, 2026

### Overview

The inaugural release of Simple Audio Player brings comprehensive audio and media playback capabilities with full accessibility support to Windows users.

### 🎉 Core Features

#### Audio & Video Playback
Support for 20+ file formats including:
- Audio: MP3, FLAC, WAV, OGG, OPUS, AAC, AIFF, ALAC, WMA
- Video: MP4, MKV, AVI, MOV, WebM, and more
- Powered by libmpv backend for reliability

#### Playlist Management
- Create and manage playlists by opening files or entire folders
- Recursive folder scanning for comprehensive library building
- File information tracking and metadata display

#### Keyboard Accessibility
- Complete keyboard control with 50+ shortcuts
- All features accessible without mouse
- Global hotkey support even when window unfocused

#### Screen Reader Support
- Full integration with JAWS, NVDA, and Windows Narrator
- Text-to-speech announcements for playback status and user actions

#### YouTube Integration
- Search and play YouTube videos directly
- Download functionality with quality selection
- Playlist support

#### Advanced Audio Processing
- Silence removal with configurable sensitivity
- Audio normalization for consistent volume
- Playback speed control (0.5x to 6.0x)
- Volume control with 1000-step precision

#### File Management
- Rename, delete, copy files
- Mark files for batch operations
- Recently opened file restoration

#### Multi-Language Support
- English and Arabic language support
- Full UI localization including all dialogs and menus

#### Windows Integration
- File association registration
- Context menu integration
- Single-instance enforcement
- Windows media session integration

#### Customizable Interface
- Customizable keyboard shortcuts
- Theme support
- Verbosity modes (Beginner/Advanced)
- Audio device selection

### 📦 Initial Release Contents

#### Documentation
- Comprehensive user guide with complete feature documentation
- Keyboard shortcut reference
- Troubleshooting guide
- FAQ section

#### Installation Methods
- Windows Installer (MSI with Inno Setup)
- Portable ZIP version
- Source code distribution

---

## Upcoming Features (Roadmap)

### Version 1.1 - Audio Enhancement Release (Q2 2026)

#### Enhanced Audio Filters
- Equalizer with preset bands (bass, treble, presence)
- Bass and treble adjustment controls
- Reverb and spatial audio effects

#### Advanced Playlist Features
- Playlist save/load functionality
- Playlist tagging and organization
- Automatic playlist generation by artist/album/genre

### Version 1.2 - Cross-Platform Release (Q4 2026)

#### Cross-Platform Support
- Linux version (Ubuntu 20.04+)
- macOS support (macOS 10.13+)
- Unified codebase across platforms

#### Cloud Integration
- Sync playlists across devices
- Cloud storage support (Dropbox, OneDrive, Google Drive)
- Settings synchronization

### Version 1.3 - Streaming Services Release (Q1 2027)

#### Streaming Services Integration
- Spotify integration and playback
- Apple Music support
- YouTube Music support

#### Mobile Companion App
- Android remote control app
- Wireless playback control
- Remote playlist management

---

## Known Issues

### Version 1.0.1

#### Minor Issues
- **Very Large Libraries:** Scanning folders with 100,000+ files may take several minutes. This is normal behavior.
- **YouTube Search Timeout:** Slow internet connections (under 1 Mbps) may experience timeout. Increase timeout value in advanced settings.
- **Audio Device Switching:** Some audio devices require system restart for full compatibility after switching.

#### Platform-Specific Issues
- **Windows 7:** Some modern codecs may not be supported. Update Windows Media Feature Pack if needed.
- **High DPI Displays:** Some UI elements may appear blurry on 200%+ DPI displays. Workaround: Disable DPI scaling in application properties.

#### Screen Reader Issues
- **NVDA + High Volume Files:** Announcements may lag when playing files with many metadata tags.
- **Windows Narrator:** Some menu items may not be announced. Use Tab key to navigate instead.

### Common Workarounds

| Issue | Workaround |
|-------|-----------|
| No sound | Check Windows audio device in Settings → Audio Device tab |
| Screen reader not working | Ensure JAWS/NVDA started before launching application |
| Application crashes | Disable silence removal and audio normalization in Settings |
| YouTube fails | Check internet connection and update yt-dlp via Tools → Update YouTube Components |

### Reporting Issues

If you encounter any bugs or issues not listed here:

1. Visit [GitHub Issues](https://github.com/kamalyaser31/simple-player/issues)
2. Check if issue already reported
3. Provide detailed reproduction steps
4. Include application version (Help → About)
5. Include Windows version and audio device details

---

## Version History Summary

| Version | Release Date | Focus | Status |
|---------|--------------|-------|--------|
| 1.0.1 | February 22, 2026 | Stability & Enhancement | Current |
| 1.0.0 | January 15, 2026 | Initial Release | Legacy |

---

## Statistics

### Current Version (1.0.1)

- **Total Features:** 80+
- **Keyboard Shortcuts:** 80+
- **Supported Audio Formats:** 10+
- **Supported Video Formats:** 13+
- **Languages Supported:** 2 (English, Arabic)
- **Lines of Code:** ~10,000+
- **Accessibility Features:** Full JAWS/NVDA/Narrator support

### Development Timeline

- **Version 1.0.0** - 1 year development
- **Version 1.0.1** - 1 month stabilization & enhancement
- **Future versions** - Active development roadmap

---

## How to Update

### Automatic Update

1. Go to `Help → Check for Updates`
2. Application will check for latest version
3. Download and install update if available
4. Restart application

### Manual Update

1. Visit [GitHub Releases](https://github.com/kamalyaser31/simple-player/releases)
2. Download latest version
3. Run installer or extract portable version
4. Existing settings and playlists automatically migrated

---

## Support & Feedback

### Getting Help

- **Documentation:** [User Guide](docs/en/userguide.html)
- **Bug Reports:** [GitHub Issues](https://github.com/kamalyaser31/simple-player/issues)
- **Feature Requests:** [GitHub Issues](https://github.com/kamalyaser31/simple-player/issues)
- **Email:** kamalyaser31@gmail.com
- **Telegram:** [@kamalyaser31](https://t.me/kamalyaser31)

### Contributing

The project is open-source and welcomes contributions:

1. Fork repository on GitHub
2. Create feature branch
3. Submit pull request with detailed description
4. Discuss changes with project maintainers

---

## License & Attribution

**Simple Audio Player** is released under the MIT License.

### Key Components

- **wxPython:** GUI framework
- **libmpv:** Media playback engine
- **yt-dlp:** YouTube support
- **accessible_output3:** Screen reader integration

---

**Last Updated:** February 22, 2026

For the latest information, visit the [GitHub Repository](https://github.com/kamalyaser31/simple-player)
