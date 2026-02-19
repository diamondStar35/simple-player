# Simple Audio Player 

A lightweight, highly accessible media player designed for keyboard efficiency and seamless screen reader compatibility. Whether playing local audio files or streaming directly from YouTube, it offers precise control, advanced audio filtering, and a distraction-free experience.

**Developed by:** Kamal Yaser
**Contact:** [Telegram](https://t.me/kamalyaser31) | [Email](mailto:kamalyaser31@gmail.com)

---

## ✨ Key Features

* **💯 Accessibility First:** Fully optimized for screen readers (using `accessible_output3`) with spoken feedback for actions like volume changes, speed adjustments, and playback status.
* **⌨️ Keyboard Driven:** Extensive customizable local and global keyboard shortcuts. Navigate your library entirely without a mouse.
* **🌐 YouTube Integration:** Native support for searching, streaming (audio-only by default), and downloading YouTube videos and playlists using `yt-dlp` and `Deno`.
* **🎛️ Advanced Audio Filters:**
  * **Dynamic Normalization & Limiter:** Balances audio levels automatically to prevent sudden loud noises and clipping.
  * **Silence Removal:** Uses FFmpeg's `silenceremove` to automatically skip dead air in podcasts or lectures (highly customizable).
  * **Mono Downmix:** Easily combine left and right audio channels.
* **🔁 Precise Playback Control:** A-B looping, custom jump percentages, variable playback speed (0.5x to 4.0x), and customizable seek steps.
* **📁 File Management:** Mark, copy, move, rename, and delete physical files directly from the player. 
* **🔄 Auto-Updater:** Built-in update system that pulls the latest releases directly from GitHub.

---

## 🚀 Installation & Setup

### Prerequisites
* **Python 3.8+** (if running from source)
* **MPV Engine:** Requires the MPV shared library (`mpv-1.dll` on Windows) accessible in your system PATH or app directory.

### Running from Source
1. Clone the repository:
   ```bash
   git clone [https://github.com/kamalyaser31/simple-player.git](https://github.com/kamalyaser31/simple-player.git)
   cd simple-player

```

2. Install the required Python dependencies:
```bash
pip install -r requirements.txt

```


*(Main dependencies include: `wxPython`, `python-mpv`, `pynput`, `Youtube-python`)*
3. Run the application:
```bash
python SimpleAudioPlayer.py

```



### First Launch

On your first launch, if you plan to use the YouTube features, go to **Preferences (`Ctrl+P`) > YouTube** and click **Download YouTube components**. This will automatically fetch the latest `yt-dlp.exe` and `deno.exe`.

---

## 🎮 Default Keyboard Shortcuts

Simple Audio Player is designed to be used entirely via the keyboard. Here are a few essential default shortcuts:

### Playback

* `Space` - Play / Pause
* `Left / Right Arrows` - Seek Backward / Forward
* `Up / Down Arrows` - Volume Up / Down
* `Shift + Up / Down` - Volume Maximize / Minimize
* `Ctrl + Up / Down` - Increase / Decrease Speed
* `Alt + Y` - Reset Speed to 1.0x
* `[` and `]` - Set A-B Loop Start / End (`Backspace` to clear)

### Navigation & Files

* `Ctrl + O` - Open File
* `Ctrl + Shift + O` - Open Folder
* `Ctrl + Shift + Y` - Open YouTube Link
* `Ctrl + Y` - Search YouTube
* `F2` - View Opened Files (Playlist)
* `Tab` / `Shift + Tab` - Next / Previous Track
* `Ctrl + K` - Mark Current File (for batch moving/deleting)

### Spoken Announcements (Screen Reader)

* `V` - Announce Volume
* `E` - Announce Elapsed Time
* `R` - Announce Remaining Time
* `T` - Announce Total Duration
* `P` - Announce Percentage Completed
* `S` - Announce Current Speed
* `F` - Announce File Info (Press multiple times to copy path)

> **Note:** All shortcuts can be remapped in the **Preferences > Keyboard Shortcuts** menu. You can also assign **Global Shortcuts** that work even when the player is minimized!

---

## ⚙️ Advanced Configuration

### Silence Removal

Perfect for listening to lectures or audiobooks. Go to **Preferences > Audio > Silence removal** to enable it. Checking "Show advanced settings" allows you to tweak the FFmpeg detection thresholds (Peak vs RMS), minimum duration, and window size to perfectly match your audio source.

### File Associations

You can set Simple Audio Player as your default media player on Windows. Go to **Preferences > General** and click **Register file extensions** to add it to your Windows context menu ("Play with Simple Audio Player").

---

## 🛠️ Built With

* [wxPython](https://wxpython.org/) - GUI toolkit
* [MPV (python-mpv)](https://github.com/jaseg/python-mpv) - Core media engine
* [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube extraction
* [pynput](https://github.com/moses-palmer/pynput) - Global keyboard hooks
* FFmpeg - Audio filtering (built into MPV)
