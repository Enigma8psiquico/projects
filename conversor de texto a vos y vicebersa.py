#!/usr/bin/env python
"""
# convertir texto a vos
import pyttsx3

engine = pyttsx3.init()
engine.say("hola mundo")
engine.runAndWait()

# convertir vos a texto
import speech_recognition as sr

r = sr.Recognize()

with sr.Microphone() as source:
    print("escuchando..")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="es")
    except Exception as e:
        print("no te entendi")

"""
import time
import speech_recognition as sr
from dataclasses import dataclass
import pyttsx3

@dataclass
class SpeechModule(object):
    """docstring for SpeechModule"""
    # rate = velocidad de habla
    def __init__(self,voice=0,volume=1,rate=125):
        self.engine=pyttsx3.init()
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume",volume)

        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[voice].id)

    def talk(self,text):
        self.engine.say(text)
        print(text)
        self.engine.runAndWait()
        

@dataclass
class VoiceRecognitionModule(object):
    """docstring for VoiceRecognitionModule"""
    def __init__(self,key=None):
        self.key = key
        self.r = sr.Recognizer()

    def recognize(self):
        with sr.Microphone() as source:
            print("escuchando...")
            audio =self.r.listen(source)

            try:
                text = self.r.recognize_google(audio, key = self.key, language = "es")
                return text
            except Exception as e:
                return None

speech = SpeechModule()            
recognition = VoiceRecognitionModule()

while True:
    text = recognition.recognize()
    if text: 
        speech.talk(text)
    time.sleep(1)