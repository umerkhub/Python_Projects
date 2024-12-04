from typing import Any, Generator

import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser as wb
import wikipedia
import pyjokes
import pyautogui
import psutil
import pyaudio
from speech_recognition import AudioData

import musicLibrary  # Assumes this module contains a `music` dictionary with song names and links

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def wish_user():
    """Greet the user based on the time of day."""
    hour = datetime.datetime.now().hour
    speak("Welcome back, Sir!")
    if 6 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    elif 18 <= hour < 24:
        speak("Good evening!")
    else:
        speak("Good night!")
    speak("Jarvis at your service. How can I assist you?")

def listen():
    """Capture audio input from the user and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as s:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            a = recognizer.listen(s, timeout=5, phrase_time_limit=5)
            query = recognizer.recognize_google(a, language='en-in')
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please repeat.")
        except sr.RequestError:
            speak("Network error. Please check your connection.")
        return None

def tell_time():
    """Tell the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak(f"The current time is {current_time}.")

def tell_date():
    """Tell the current date."""
    now = datetime.datetime.now()
    speak(f"Today's date is {now.day} {now.strftime('%B')} {now.year}.")

def take_screenshot():
    """Take a screenshot and save it."""
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    speak("Screenshot taken.")

def get_joke():
    """Tell a joke."""
    joke = pyjokes.get_joke()
    speak(joke)

def check_cpu():
    """Provide CPU usage and battery status."""
    usage = psutil.cpu_percent()
    battery = psutil.sensors_battery()
    speak(f"CPU usage is at {usage} percent.")
    speak(f"Battery is at {battery.percent} percent.")


def execute_command(c):
    """Execute tasks based on the user's command."""
    if "time" in c:
        tell_time()
    elif "date" in c:
        tell_date()
    elif "wikipedia" in c:
        speak("Searching Wikipedia...")
        c = c.replace("wikipedia", "")
        try:
            result = wikipedia.summary(c, sentences=3)
            print(result)
            speak(result)
        except Exception as e:
            print(e)
            speak("I couldn't fetch information from Wikipedia.")
    elif "open youtube" in c:
        wb.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "open google" in c:
        wb.open("https://www.google.com")
        speak("Opening Google.")
    elif "open instagram" in c:
        wb.open("https://www.instagram.com")
        speak("Opening Instagram.")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        wb.open(link)

    elif "screenshot" in c:
        take_screenshot()
    elif "cpu" in c:
        check_cpu()
    elif "joke" in c:
        get_joke()
    elif "quit" in c or "exit" in c:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("I'm sorry, I can't help with that yet.")

if __name__ == "__main__":
    r = sr.Recognizer()
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)  # Adjusted timeout settings
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Present")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)  # Adjusted timeout settings
                    command = r.recognize_google(audio)
                    execute_command(command)  # Fixed undefined function
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError:
            print("Network error. Please check your connection.")
        except Exception as e:
            print(f"Error: {e}")

