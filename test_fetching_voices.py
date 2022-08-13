# Get info on avaliable voices on your machine from SAPI 5 API (pyttsx3)

# Text to speech conversion modules
import speech_recognition as sr
import pyttsx3
import datetime

# Initialize the converter
converter = pyttsx3.init()

voices = converter.getProperty('voices')
  
for voice in voices:
    # to get the info. about various voices in our PC 
    print("Voice:")
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s" %voice.languages)