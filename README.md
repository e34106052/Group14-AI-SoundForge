
# 🎵 AI SoundForge

**AI SoundForge** is an interactive music generation application that integrates a state-of-the-art AI music generator and a genre classifier. With a user-friendly GUI, you can select a music genre and length, generate a unique track, listen to it, and provide feedback — all within seconds.

---

## 📦 Features

- 🎼 Select custom **music genre** and **duration**
- 🔊 Instantly **play or pause** the generated music
- 👍👎 Provide feedback to like or **regenerate** the music
- 🌓 Switch between **Light / Dark** theme
- 📁 Choose your **music save folder**

---

## 🛠️ Requirements

Please ensure the following Python packages are installed:

```bash
pip install flet transformers torchaudio torch scikit-learn librosa scipy soundfile
```

---

## 🚀 How to Run

1. Open your **Terminal** or **Command Prompt**
2. Navigate to the project directory containing `main.py`, for example:

```bash
cd path/to/your/project
```

3. Run the app:

```bash
python main.py
```

A new GUI window will launch automatically.

---

## 🧭 User Guide

1. On the **Initial Screen**, click `🎼 Generate Music` to enter the Interaction Page
2. Select your desired **Genre** and **Length**
3. Click `Generate Music` to create your track
4. Use the `▶️ Play` and `⏸ Pause` buttons to control playback
5. Press `👍 Like` to show appreciation or `👎 Dislike` to regenerate a new track with the same style
6. Use the `⚙️ Settings` screen to set the **save folder** and toggle the **theme**

---

## 🖼️ Genre Images (unfinished)

Each generated result is accompanied by a genre-related image, randomly selected from:

```
/image/
├── blues/
├── classical/
├── country/
├── disco/
├── hiphop/
├── jazz/
├── metal/
├── pop/
├── reggae/
└── rock/
```

Place `.jpg` or `.jpeg` images in each corresponding genre folder.

---

## 📂 Output Storage

Generated `.wav` music files will be saved to the folder you selected in the **Settings** page.  
If no folder is set, the app will use a default directory in the execution folder.

---

## 🙋 FAQ

- **Music not playing?**  
  Make sure the file was successfully generated and the audio source is set correctly.

- **Generation is slow or unresponsive?**  
  The music model may take a few seconds to process — please wait patiently.

- **Can't import `flet`?**  
  Run `pip install flet` to install the required GUI library.
  (If you have issues with Flet 0.28.3, try installing version 0.24.1 with `pip install flet==0.24.1`)
  
---

## 📧 Contact

For suggestions, feedback, or bug reports, feel free to open an issue or contact the developer 🙌
