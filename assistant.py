import pyttsx3
from selenium import webdriver 
import os
import random2

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def assisstant(command):
    if command == command:
        if command == str("random number"):
            print(2)
        if command == str("Open YT"):
            browser = webdriver.Chrome()
            browser.get('https://www.youtube.com/')
        else:
            print("Error: Unknown command")
            retry_input = input("Do you want to retry(y/n): ")
            if retry_input == ("y"):
                assisstant(command_input)
            if retry_input == ("n"):
                exit

command_input = input("Enter command: ")
assisstant(command_input)