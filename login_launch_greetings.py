#               Author: Ettore Bartalucci, 13.08.2022 Eschweiler

#  Greet user when logging in to the pc and play ACDC while loading modules

# Text to speech conversion modules
import speech_recognition as sr
import pyttsx3
import datetime
# Audio reproduction modules
from playsound import playsound
   

# initialize SAPI 5 and engines, fetch voices
engine=pyttsx3.init('sapi5')
engine.setProperty('rate',160) 
engine.setProperty('volume',1.0)
voices=engine.getProperty('voices')
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
engine.setProperty('voice', voice_id)

# Text to speech conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Greetings on startup
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("Welcome back to the office. All systems will be operational shortly.")    

wishMe()

# Play music ACDC
playsound(r'C:\Users\ettor\Desktop\Login_greetings\shoot-to-thrill-trimmed.mp3')

# System ready
def ready():
    speak("Your machine is now ready. Have a nice day.")

ready()