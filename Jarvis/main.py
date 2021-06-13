import pyttsx3 
import speech_recognition as sr
import dataclasses
import wikipedia 
import webbrowser
import os
import smtplib
import datetime

print('Initializing Jarvis')

MASTER=" SUBHA "

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
speak('Initializing jarvis')

def wishme():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour< 12:
        speak("good morning" + MASTER)
    elif hour>=2 and hour< 18:
        speak("good after noon master" + MASTER)
    else:
        speak("good evening" + MASTER)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        audio = r.listen(source)  
    try :
        print("Recognizing....")
        query = r.recognize_google(audio, language = "en-in")
        print(f"User said:{query}\n" )  
    except Exception as e:
        print("say that again please")
        query=None

    return query

wishme()
queryy = take_command()
print(queryy)


if "wikipedia" in query.lower():
    speak('searching wikipedia....')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query,sentences =2)
    speak(results)

