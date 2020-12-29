import pyttsx3
import scraper
import tasks
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

command_input = input("Enter command: ")
assisstant(command_input)