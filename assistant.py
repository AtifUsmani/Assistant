import pyttsx3
import scraper
import tasks
import speech_recognition as sr
import encrypter
import cpu
import music
import os
from cryptography.fernet import Fernet
import webbrowser
import time
from datetime import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
key = Fernet.generate_key()
f = Fernet(key)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
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
        print(e)
        print("Unable to Recognize your voice")
        return "None"
    
    return query

def assisstant(command):
    if command == str("Open YT"):
        scraper.youtube()
        speak("Opening Youtube")
    if command == str("Open Music app"):
        scraper.YT_music()
        speak("Opening YT Music")
    if command == str("Open Github"):
        scraper.Github()
        speak("Opening Github")
    if command == str("Enter a task = str"):
        task_input = input(str("Enter a new task: "))
        tasks.text(task_input)
        speak("Changes saved")
    if command == str("Enter a task = int"):
        task_input = input("Enter a new task: ")
        task_input_float = int(float(task_input))
        tasks.text(task_input_float)
        speak("Changes saved")
    if command == str("Encrypt"):
        encrypter_input = input(str("Enter a string to encrypt: "))
        encrypter.encrypt(bytes(encrypter_input, encoding='utf-8'))
        # encrypter_input = message
    if command == str("Decrypt"):
        decrypter_input = input(str("Enter to decrypt: "))
        encrypter.decrypt(bytes(decrypter_input, encoding='utf-8'))
    if command == str("Play some music"):
        music_choice = input(str("Should I open YT Music or Play locally?"))
        if music_choice == str("Play from YT Music"):
            scraper.YT_music()
        elif music_choice == str("Play Locally"):
                # pick an external mp3 player you have
                music.play_music("/home/atif/Documents/MyProjects/Assistant/Music/Post Malone - Better Now.mp3")
# command_input = input("Enter command: ")
# assisstant(command_input)

if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()

    while True:

        query = takeCommand().lower()
        if 'music' in query:
            speak("Do you want to YT Music or play locally")
            if 'locally' in query:
                pass
            elif 'music' in query:
                webbrowser.open("music.youtube.com")
        elif 'youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        elif 'github' in query:
            webbrowser.open("https://github.com/AtifUsmani/Assistant")
        elif 'new string' in query:
            speak("Plz enter what you want to encrypt")
            task_string =  input(str("Plz enter what you want to encrypt: "))
            tasks.text(task_string)
            speak("Changes saved")
        elif 'new integer' in query:
            speak("Plz enter what you want to encrypt")
            task_input = input("Enter a new task: ")
            task_input_float = int(float(task_input))
            tasks.text(task_input_float)
            speak("Changes saved")
        elif 'time' in query:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)
            speak_current_time = ("Current Time =", current_time)
            speak(speak_current_time)