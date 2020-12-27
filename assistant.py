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
    # speak a random number
    if command == str("random number"):
        print(2)
    if value_for_number == value_for_number:
        print(value_for_number)
        speak(value_for_number)

command_input = input("Enter command: ")
if command_input == str("Write a number"):
    value_for_number = input("Enter number: ")
assisstant(command_input)