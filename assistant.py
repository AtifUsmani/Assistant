import pyttsx3
import scraper
import tasks
import speech_recognition as sr
import encrypter
from cryptography.fernet import Fernet
import cpu

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
key = Fernet.generate_key()
f = Fernet(key)


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
command_input = input("Enter command: ")
assisstant(command_input)
