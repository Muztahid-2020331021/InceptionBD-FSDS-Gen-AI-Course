# JARVIS-Voice-Assistant-System

JARVIS is a Python-based voice assistant that can interact with the user through speech recognition, perform tasks like opening applications, searching on Google or Wikipedia, playing music randomly, telling jokes, and having small talk.

This project uses speech recognition and text-to-speech (TTS) to provide a hands-free assistant experience similar to Iron Man's JARVIS.


## 🛠 Features

- Greet the user according to the time of day (morning, afternoon, evening)

- Recognize voice commands using Google Speech Recognition

- Speak responses using pyttsx3

- Time & Date announcements

- Wikipedia search with spoken summary

- Open websites like Google, Facebook, YouTube

- Play random music from a specified folder

- Open system applications: Calculator, Notepad, CMD

- Open Calendar (Google Calendar via browser)

- Tell jokes and respond to basic small talk

- Exit gracefully with a voice command



## 💻 Requirements 

- Python 3.11 or higher 


## How to run? 

1. Create a virtual environment:

   ```bash
   conda create -n jarvis python=3.11 -y
   ```

2. Activate virtual environment:

   ```bash
   conda activate jarvis
   ```

3. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the JARVIS script:

   ```bash
   python jarvis.py
   ```

## Example Voice Commands
- For Searching something on website:
   - First say, "Enter web search mode". Then it will enter web search mode.
   - Then say what you want to search.
   - If you want to exit, then say "exit" or "close". Then it will close the system mode 
   come back to general mode.
- For Opening an application on your system:
   - First say, "Enter system mode". Then it will enter system mode.
   - Then say the name of the application that you want to open.
   - If you want to exit, then say "exit" or "close". Then it will close the system mode 
   come back to general mode.
- Other casual conversation like:
   - Tell me a joke.

## 👨‍💻 Author

**Md Muztahid Hassan**

Inspired by Tony Stark's JARVIS


### 📜 License

This project is open-source and free to use for learning purposes.