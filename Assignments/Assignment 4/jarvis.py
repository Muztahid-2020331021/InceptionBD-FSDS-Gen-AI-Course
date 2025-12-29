import speech_recognition as sr 
import pyttsx3 
import logging 
import os 
import datetime 
import wikipedia 
import webbrowser 
import random 
import subprocess 
import requests
import psutil
import pyautogui
import google.generativeai as genai 





LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"
MUSIC_DIR = r"D:\Desktop\InceptionBD\InceptionBD-FSDS-Gen-AI-Course\Assignments\Assignment 4\Music"
SCREENSHOT_DIR = r"D:\Desktop\InceptionBD\InceptionBD-FSDS-Gen-AI-Course\Assignments\Assignment 4\Screenshots"
GEMINI_API_KEY = "Your Gemini API Key"
OPENWEATHER_API_KEY = "Your openweather api key"
NEWSDATA_API_KEY = "Your newsdata api key"


news_cache = []


if GEMINI_API_KEY != "YOUR_GEMINI_API_KEY_HERE":
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")


# Logging configuration 
os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)



# Activating voice from our system 
engine = pyttsx3.init("sapi5") 
engine.setProperty('rate', 170)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)


# This is speak function
def speak(text):
    """Converts text to voice
    args:
        text
    return 
        voice
    """
    engine.say(text)
    engine.runAndWait()



# This function recognize the speech and convert it to text 

def takeCommand():
    """Takes microphone input and returns string"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        logging.info(e)
        print("Say that again please")
        return "None"
    
    return query




def greeting():
    """Greets the user based on time"""
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon sir!")
    else:
        speak("Good night sir!")
    
    speak("I am Jarvis. System is online. How may I help you?")



def get_weather(city_name):
    """Fetches weather from OpenWeatherMap"""
    try:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = f"{base_url}appid={OPENWEATHER_API_KEY}&q={city_name}&units=metric"
        response = requests.get(complete_url)
        x = response.json()
        
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak(f" The temperature in {city_name} is {current_temperature} degrees Celsius with {weather_description}.")
            logging.info(f"Weather fetched for {city_name}")
        else:
            speak("City not found.")
    except Exception as e:
        speak("I encountered an error fetching the weather.")
        logging.error(f"Weather error: {e}")




def play_music():
    """Plays random music from directory"""
    try:
        if os.path.exists(MUSIC_DIR):
            songs = os.listdir(MUSIC_DIR)
            if songs:
                random_song = random.choice(songs)
                speak(f"Playing: {random_song}")
                os.startfile(os.path.join(MUSIC_DIR, random_song))
                logging.info(f"Playing music: {random_song}")
            else:
                speak("No music files found in your music directory.")
        else:
            speak("The music directory path is incorrect.")
    except Exception as e:
        speak("Sorry sir, I could not play the music.")
        logging.error(f"Music error: {e}")


def get_news_bd(category):
    """Fetches news and caches them for interactive reading"""
    global news_cache
    try:
        base_url = f"https://newsdata.io/api/1/news?apikey={NEWSDATA_API_KEY}&country=bd&language=en"
        if category != "general":
            base_url += f"&category={category}"
            
        response = requests.get(base_url)
        data = response.json()

        if data["status"] == "success":
            results = data["results"]
            news_cache = results[:3] # Store top 3 articles in memory
            
            if not news_cache:
                speak("I couldn't find any news for that category.")
                return

            speak(f"Here are the top {category} headlines.")
            for i, article in enumerate(news_cache, 1):
                title = article.get('title', 'No Title')
                speak(f"Number {i}: {title}")
                print(f"{i}. {title}")
            
            speak("Which one would you like me to read in detail?")
        else:
            speak("I had trouble communicating with the news server.")
            logging.error(f"NewsData Error: {data}")

    except Exception as e:
        speak("I encountered an error fetching the news.")
        logging.error(f"News connection error: {e}")




def gemini_model_response(user_input):
    """Generates AI response using Gemini"""
    if GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        return "Please configure your Gemini API Key."
    try:
        prompt = f"You are JARVIS, a helpful assistant. User asks: {user_input}. Answer concisely in plain text."
        response = model.generate_content(prompt)
        return response.text.replace("*", "") 
    except Exception as e:
        logging.error(f"Gemini Error: {e}")
        return "I am having trouble connecting to the AI brain."


# For system status
def get_system_stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()
    status_report = f"CPU usage is at {cpu_usage} percent. RAM usage is at {ram_usage} percent."
    if battery:
        plugged = "plugged in" if battery.power_plugged else "not plugged in"
        status_report += f" Battery is at {battery.percent} percent and {plugged}."
    else:
        status_report += " No battery detected."
        
    return status_report


def volume_control(query):
    if "mute" in query or "unmute" in query:
        speak("Toggling sound.")
        pyautogui.press("volumemute")
    
    elif "up" in query or "increase" in query:
        speak("Increasing volume.")
        # Press the key 5 times for a noticeable change
        for _ in range(5): 
            pyautogui.press("volumeup")
    
    elif "down" in query or "decrease" in query:
        speak("Decreasing volume.")
        # Press the key 5 times for a noticeable change
        for _ in range(5): 
            pyautogui.press("volumedown")
    
    else:
        speak("Sure, adjusting volume.")
        pyautogui.press("volumeup")



            

if __name__ == "__main__":
    greeting()
    
    while True:
        # 1. Listen for voice
        query = takeCommand().lower()
        
        # 2. Filter out failed recognitions
        if query == "None":
            continue

        # --- WAKE WORD CHECK ---
        # If the user didn't say "Jarvis", ignore the command completely.
        if "jarvis" not in query:
            continue
        
        # --- CLEANUP ---
        # Remove "jarvis" so "Jarvis open google" becomes just "open google"
        query = query.replace("jarvis", "").strip()

        # If user only said "Jarvis" with no command, ask what they need
        if not query:
            speak("Yes sir?")
            continue

        # --- COMMAND PROCESSING (Uses cleaned 'query') ---

        # Identity & Small Talk
        if "your name" in query:
            speak("My name is Jarvis.")
        elif "how are you" in query:
            speak("Systems are functioning at 100 percent.")
        elif "who made you" in query:
            speak("I was created by Muztahid.")

        # Features
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {strTime}")
        elif "date" in query:
            strDate = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today is {strDate}")

        # Weather
        elif "weather" in query:
            city = "Dhaka" # Default
            if "in" in query:
                # "weather in bogura" -> splits to ["weather ", " bogura"]
                city = query.split("in")[-1].strip()
            get_weather(city)

        # Web Browsing
        elif "youtube" in query:
            speak("Accessing YouTube...")
            term = query.replace("open", "").replace("search", "").replace("youtube", "").replace("on", "").replace("for", "").strip()
            if term:
                speak(f"Searching for {term} on YouTube")
                webbrowser.open(f"https://www.youtube.com/results?search_query={term}")
            else:
                webbrowser.open("https://www.youtube.com")

        elif "google" in query:
            speak("Accessing Google...")
            term = query.replace("open", "").replace("search", "").replace("google", "").replace("on", "").replace("for", "").strip()
            if term:
                speak(f"Searching for {term} on Google")
                webbrowser.open(f"https://www.google.com/search?q={term}")
            else:
                webbrowser.open("https://www.google.com")

        # Direct Sites
        elif "facebook" in query:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")
        elif "linkedin" in query:
            speak("Opening LinkedIn")
            webbrowser.open("https://www.linkedin.com")
        elif "github" in query:
            speak("Opening GitHub")
            webbrowser.open("https://www.github.com")

        # System Control: Close Apps
        elif "close" in query:
            if "notepad" in query:
                speak("Closing Notepad")
                os.system("taskkill /f /im notepad.exe")
            
            elif "calculator" in query:
                speak("Closing Calculator")
                os.system("taskkill /f /im CalculatorApp.exe")
            
            elif "chrome" in query or "browser" in query:
                speak("Closing Browser")
                os.system("taskkill /f /im chrome.exe")
            
            else:
                speak("I am not sure which application to close.")

        # System Control: Open Apps
        elif "open" in query or "start" in query: 
            if "notepad" in query:
                speak("Opening Notepad")
                subprocess.Popen("notepad.exe")
            elif "vscode" in query or "code" in query:
                speak("Opening Visual Studio Code")
                try:
                    subprocess.Popen("code", shell=True) 
                except:
                    speak("VS Code path not found.")
            elif "calculator" in query:
                speak("Opening calculator")
                subprocess.Popen("calc.exe")
            elif "terminal" in query:
                speak("Opening Terminal")
                subprocess.Popen("wt.exe")
            elif "calendar" in query:
                speak("Opening Calendar")
                subprocess.Popen("start outlookcal:", shell=True) 
            elif "cmd" in query:
                speak("Opening Command Prompt")
                subprocess.Popen("start cmd.exe", shell=True)

        # Wikipedia
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("according to wikipedia", "")
            query = query.replace("jarvis who is", "")
            try:
                results = wikipedia.summary(query, sentences=1)
                speak(f"According to Wikipedia: {results}")
            except:
                speak("I couldn't find that page.")

        # News Reader
        elif "news" in query:
            speak("Checking the latest headlines...")
            category = "general" 
            if "tech" in query: category = "technology"
            elif "sport" in query: category = "sports"
            elif "business" in query: category = "business"
            elif "politics" in query: category = "politics"
            elif "health" in query: category = "health"
            elif "science" in query: category = "science"
            elif "entertainment" in query: category = "entertainment"
            
            get_news_bd(category)

        # Interactive News Reader (Reading specific articles)
        elif "read" in query and ("first" in query or "second" in query or "third" in query):
            if not news_cache:
                speak("I haven't fetched any news yet. Ask me for headlines first.")
            else:
                idx = -1
                if "first" in query: idx = 0
                elif "second" in query: idx = 1
                elif "third" in query: idx = 2
                
                if 0 <= idx < len(news_cache):
                    article = news_cache[idx]
                    title = article.get('title', '')
                    summary = article.get('description') or article.get('content') or "No details available."
                    speak(f"Reading article: {title}")
                    speak(summary)
                    speak("End of article.")
                else:
                    speak("I only have three articles in memory.")

        # Music
        elif "play music" in query or "song" in query:
            play_music()

        # Jokes
        elif "joke" in query:
            jokes = [
                "Why do Python programmers prefer dark mode? Because light attracts bugs.",
                "I am not lazy, I am just in energy saving mode.",
                "Artificial intelligence is no match for natural stupidity."
            ]
            speak(random.choice(jokes))
        
        # System Status
        elif "system status" in query or "cpu usage" in query or "battery" in query:
            report = get_system_stats()
            speak(report)

        # Screenshot
        elif "screenshot" in query:
            speak("Taking screenshot")
            if not os.path.exists(SCREENSHOT_DIR):
                os.makedirs(SCREENSHOT_DIR)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join(SCREENSHOT_DIR, f"screenshot_{timestamp}.png")
            img = pyautogui.screenshot()
            img.save(filename)
            speak("Screenshot saved.")

        # Volume Control
        elif "volume" in query or "mute" in query or "unmute" in query:
            volume_control(query)

        # Exit
        elif "exit" in query or "shutdown" in query or "goodbye" in query:
            speak("Shutting down. Have a good day, sir.")
            exit()

        # Fallback to Gemini
        else:
            response = gemini_model_response(query)
            speak(response)