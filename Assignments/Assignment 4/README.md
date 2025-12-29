# 🤖 JARVIS Voice Assistant

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success.svg?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

> *"Just a rather very intelligent system."*

**JARVIS** is a Python-based voice assistant designed to automate tasks and provide a hands-free interaction experience. Inspired by Iron Man's assistant, it features a **smart wake word**, advanced system control, interactive news reading, real-time weather, and AI-powered conversation.

---

## 📑 Table of Contents
- [✨ Features and Voice Commands](#features-and-voice-commands)
- [💻 Requirements](#requirements)
- [⚙️ Installation](#installation)
- [🚀 Usage](#usage)
- [👨‍💻 Author](#author)
- [📜 License](#license)

-----

## <a id="features-and-voice-commands"></a> ✨ Features & Voice Commands

### 🎙️ Smart Wake Word
Jarvis now runs in a passive listening mode. He will only execute commands when addressed directly.
- **🗣️ Usage:**
  - *"Jarvis, what is the time?"*
  - *"Jarvis, open Google."*
  - *(Background noise is ignored unless "Jarvis" is spoken)*

### 🧠 Artificial Intelligence (The "Brain")
Powered by **Google Gemini** and **Wikipedia**, Jarvis can answer complex questions, summarize topics, and chat intelligently.

  - **Library:** `google.generativeai`, `wikipedia`
  - **🗣️ Command Guide:**
      - *"Jarvis, who is Elon Musk?"* (Searches Wikipedia)
      - *"Jarvis, tell me about Black Holes."* (Wikipedia summary)
      - *"Jarvis, how do I bake a cake?"* (Ask Gemini AI)
      - *"Jarvis, write a python code for sorting."* (Ask Gemini AI)

### 🌤️ Real-time Weather
Fetches live weather updates for Dhaka city globally using the OpenWeatherMap API.

  - **API:** OpenWeatherMap
  - **Library:** `requests`
  - **🗣️ Command Guide:**
      - *"Jarvis, what is the weather?"* (Defaults to Dhaka)
      - *"Jarvis, weather in **Sylhet**"*
      - *"Jarvis, weather in **London**"*

### 🔊 Volume & Media Control

Control your system audio levels using keyboard simulation. This feature mimics physical media keys to ensure compatibility with all Windows versions.

* **Library:** `pyautogui`
* **🗣️ Command Guide:**
* *"Jarvis, volume up"* (Increases volume)
* *"Jarvis, volume down"* (Decreases volume)
* *"Jarvis, mute"* / *"Jarvis, unmute"* (Toggles system sound)

### 📰 Interactive News Reader 
Get the latest headlines and ask Jarvis to read specific articles in detail.

  - **API:** `NewsData.io` 
  - **🗣️ Command Guide:**
      - *"Jarvis, tell me the news"* (Fetches top headlines)
      - *"Jarvis, give me sports news"*
      - *"Jarvis, read the first one"* (Reads the full summary of article #1)
      - *"Jarvis, read number two"*

### 🌐 Web & Connectivity
Jarvis can navigate the web, open specific sites, or perform direct searches.

  - **Library:** `webbrowser`
  - **🗣️ Command Guide:**
      - *"Jarvis, open Google"*
      - *"Jarvis, search for **Cricket** on Google"* (Direct search query)
      - *"Jarvis, search for **Tom and Jerry** on YouTube"* (Direct video search)
      - *"Jarvis, open Facebook"* / *"Open LinkedIn"* / *"Open GitHub"*

### 🖥️ System Automation
Control your local Windows applications hands-free.

  - **Library:** `os`, `subprocess`
  - **🗣️ Command Guide:**
      - *"Jarvis, open Notepad"* / *"Close Notepad"*
      - *"Jarvis, open VS Code"*
      - *"Jarvis, open Terminal"*
      - *"Jarvis, take screenshot"* (Saves timestamped image to your folder)

### 💻 System Health Monitoring
Real-time tracking of your PC's vital statistics.

  - **Library:** `psutil`
  - **🗣️ Command Guide:**
      - *"Jarvis, system status"* (Reports CPU, RAM, and Battery)
      - *"Jarvis, how is my battery?"*

----

## <a id="requirements"></a> 💻 Requirements

- **Python**: version `3.11` or higher
- **Microphone**: For voice input
- **Internet Connection**: For web scraping and recognition APIs
- **OS**: Windows (Required for `pycaw` audio control and `pyttsx3` sapi5 drivers)

-----

## <a id="installation"></a> ⚙️ Installation & Setup

### 1️⃣ Create a Virtual Environment
It is recommended to use **Conda** or **venv** to keep your project dependencies isolated.
```bash
conda create -n jarvis python=3.11 -y

```

### 2️⃣ Activate the Environment

```bash
conda activate jarvis

```

### 3️⃣ Install Dependencies

Ensure you have the `requirements.txt` file in your directory.

```bash
pip install -r requirements.txt

```

> **⚠️ Note on PyAudio:** If `pip install PyAudio` fails on Windows, install it using pipwin:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> 
> ```
> 
> 

### 4️⃣ 🔑 Configure API Keys

To unlock the full potential of JARVIS, generate free API keys from the following providers:

| Feature | Provider | Action |
| --- | --- | --- |
| **🧠 AI Brain** | Google Gemini | [Get Free API Key](https://aistudio.google.com/app/apikey) |
| **🌤️ Weather** | OpenWeatherMap | [Sign Up](https://openweathermap.org/api) |
| **📰 News** | NewsData.io | [Get Free API Key](https://newsdata.io/) |

Once you have your keys, open `jarvis.py` and replace the variables:

```python
GEMINI_API_KEY = "paste_your_gemini_key_here"
OPENWEATHER_API_KEY = "paste_your_weather_key_here"
NEWSDATA_API_KEY = "paste_your_newsdata_key_here"

```

### 5️⃣ 🚀 Run the Application

You are all set! Start the assistant with:

```bash
python jarvis.py

```

---

## <a id="usage"></a> 🚀 Usage

Run the main script:

```bash
python jarvis.py

```

1. Wait for the greeting: *"I am Jarvis. System is online."*
2. Say **"Jarvis"** followed by your command.
* *Example:* "Jarvis, what is the weather in Dhaka?"

---

## <a id="author"></a> 👨‍💻 Author

### Md Muztahid Hassan

*Inspired by Tony Stark's JARVIS*

---

## <a id="license"></a> 📜 License

This project is open-source and available for learning purposes.