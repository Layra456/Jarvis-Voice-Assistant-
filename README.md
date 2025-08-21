# 🤖 Jarvis Voice Assistant  

A simple **AI-powered voice assistant** built in Python. Jarvis can recognize your voice commands, speak responses, and perform tasks like opening websites, playing music, and more.  

---

## 📌 Features  
- 🎤 Voice recognition (using `speech_recognition`)  
- 🔊 Text-to-Speech (TTS) support with `gTTS` or `pyttsx3`  
- 🌐 Opens websites like YouTube, Google, etc.  
- 🎶 Plays music  
- 🖥️ Executes system tasks  
- ⚡ Easy to customize and extend  

---

## 🛠️ Tech Stack  
- **Language:** Python 3.x  
- **Libraries:**  
  - `speech_recognition` – Convert speech to text  
  - `gTTS` / `pyttsx3` – Convert text to speech  
  - `pygame` – Play audio  
  - `webbrowser` – Open websites  
  - `os`, `time`, `tempfile` – System utilities  

---

---

## ⚙️ Installation  

1. **Clone the repository**  
```bash
git clone https://github.com/Layra456/Jarvis-Voice-Assistant-.git
cd Jarvis-Voice-Assistant-

## 📂 Project Structure  
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python jarvis.py
