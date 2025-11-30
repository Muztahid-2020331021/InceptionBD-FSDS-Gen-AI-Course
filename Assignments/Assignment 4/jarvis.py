import speech_recognition as sr 
import pyttsx3 
import logging 
import os 
import datetime 
import wikipedia 
import webbrowser 
import random 
import subprocess 
import google.generativeai as genai 


# Logging configuration 
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

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
    """This function converts text to voice

    Args:
        text
    returns:
        voice
    """
    engine.say(text)
    engine.runAndWait()



# This function recognize the speech and convert it to text 

def takeCommand():
    """This function takes command & recognize

    Returns:
        text as query
    """
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
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir! How are you doing?")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon sir! How are you doing?")
    else:
        speak("Good Evening sir! How are you doing?")
    

    speak("I am Jarvis. Please tell me how may I help you today?")




def play_music():
    music_dir = "D:\\Desktop\\InceptionBD\\InceptionBD-FSDS-Gen-AI-Course\\Assignments\\Assignment 4\\Music"   # <-- change this to your music folder
    try:
        songs = os.listdir(music_dir)
        if songs:
            random_song = random.choice(songs)
            speak(f"Playing a random song sir: {random_song}")
            os.startfile(os.path.join(music_dir, random_song))
            logging.info(f"Playing music: {random_song}")
        else:
            speak("No music files found in your music directory.")
    except Exception:
        speak("Sorry sir, I could not find your music folder.")




def gemini_model_response(user_input):
    GEMINI_API_KEY = "AIzaSyCw3F797hTYxL5vMAhzQnbRxqUxlZdRM18"
    genai.configure(api_key=GEMINI_API_KEY) 
    model = genai.GenerativeModel("gemini-2.5-flash") 
    prompt = f"Your name is JARVIS, You act like JARVIS. Answar the provided question in short, Question: {user_input}"
    response = model.generate_content(prompt)
    result = response.text
    return result

sites = ["google", "facebook", "linkedin", "github", "youtube"]

def remove_common_words(text):
    common_words = ["please", "open", "can", "would", "jarvis", "just", "on", "in", "and"]
    text = text.split()
    for i in common_words:
        if i in text:
            text.remove(i)
    return " ".join(text)


def websearch():
    while True:
        speak("What do you want to search, sir?")
        text = takeCommand().lower()
        print("Web search mode...")
        if "exit" in text or "close" in text:
            speak("Exiting web search mode")
            break
        else:
            speak("I am searching")
            text = remove_common_words(text)
            if "search" in text:
                text = text.replace("search", "")
                if "google" in text:
                    text = text.replace("google", "")
                    webbrowser.open(f"https://www.google.com/search?q={text}")
                if "youtube" in text:
                    text = text.replace("youtube", "")
                    webbrowser.open(f"https://www.youtube.com/results?search_query={text}")
            else:
                not_found = True 
                for site in sites:
                    if site in text:
                        webbrowser.open(f"https://www.{site}.com/")
                        not_found = False
                        break
                if not_found:
                    webbrowser.open(f"https://www.google.com/search?q={text}")






def system_application_open():
    while True:
        speak("Which application do you want to open, sir?")
        text = takeCommand().lower()
        print("System mode...")
        if "exit" in text or "close" in text:
            speak("Exiting System mode")
            break
        else:
            text = remove_common_words(text)
            if "notepad" in text:
                speak("Opening Notepad")
                subprocess.Popen("notepad.exe")
                logging.info("User requested to open Notepad.")

            elif "vscode" in text or "visual studio code" in text:
                speak("Opening Visual Studio Code")
                try:
                    subprocess.Popen("code", shell=True) 
                except:
                    speak("I couldn't find VS Code.")
                logging.info("User requested to open VS Code.")

            elif "calculator" in text:
                speak("Opening calculator")
                subprocess.Popen("calc.exe")
                logging.info("User requested to open Calculator.")

            elif "terminal" in text:
                speak("Opening Terminal")
                subprocess.Popen("wt.exe")
                logging.info("User requested to open Terminal.")

            elif "calendar" in text or "calender" in text:
                speak("Opening Calendar")
                subprocess.Popen("start outlookcal:", shell=True) 
                logging.info("User requested to open Calendar.")

            elif "cmd" in text or "command prompt" in text:
                speak("Opening Command Prompt")
                subprocess.Popen("start cmd.exe", shell=True)
                logging.info("User requested to open CMD.")
            else:
                speak("cannot find the application")
            







greeting()

while True:
    query = takeCommand().lower()
    print(query)

    if "your name" in query:
        speak("My name is Jarvis")
        logging.info("User asked for assistant's name.")

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strTime}")
        logging.info("User asked for current time.")

    
    # Small talk
    elif "how are you" in query:
        speak("I am functioning at full capacity sir!")
        logging.info("User asked about assistant's well-being.")

    
    elif "who made you" in query:
        speak("I was created by Muztahid sir, a brilliant mind!")
        logging.info("User asked about assistant's creator.")

    
    elif "thank you" in query:
        speak("It's my pleasure sir. Always happy to help.")
        logging.info("User expressed gratitude.")

    elif "search" in query or "website" in query:
        speak("Entering Web search mode.")
        websearch()
        print("General mode...")
        logging.info("User requested to search on website")
    
    elif "application" in query or "system" in query:
        speak("Entering System mode")
        system_application_open()
        print("General mode...")
    
    # Jokes
    elif "joke" in query:
        jokes = [
            "Why don't programmers like nature? Too many bugs.",
            "I told my computer I needed a break. It said no problem, it will go to sleep.",
            "Why do Java developers wear glasses? Because they don't C sharp."
        ]
        speak(random.choice(jokes))
        logging.info("User requested a joke.")

    
    elif "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        logging.info("User requested information from Wikipedia.")

    
    elif "play music" in query or "music" in query:
        play_music()


    elif "exit" in query or "close" in query:
        speak("Thank you for your time sir. Have a great day ahead!")
        logging.info("User exited the program.")
        exit()

    else:
        response = gemini_model_response(query)
        speak(response)
        logging.info("User asked for others question")

