import speech_recognition as sr
import pyttsx3
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('opening whatsapp')
