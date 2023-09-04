import pyttsx3
import datetime
import wikipedia
import pyaudio
import speech_recognition as sr
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')  #used voices ko lena ka lia ,window API deti ha jis sa hum voice la sakta ha
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    '''speak function aik string leta ha aur us ko bolta ha'''
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Nigh")
    speak("Hello Maavia , I am your personal assistant sir. Please tell me how may I help you.")

def takecommand():
    '''this function takes microphone input from the user  amd return string output'''
    r = sr.Recognizer()
    # help to recognize the audio
    with sr.Microphone() as source: #sourece microphone ka lia use karo ga
        print("Listening...")
        r.pause_threshold = 1   # seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold = 100 # awaz kitni taz ha
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said :{query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
if __name__ == "__main__":
    wishme()
    while True:
    # if 2:
        query = takecommand().lower() # Add this line to make Jarvis speak the recognized query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query,sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'play music' in query:
            music_dir = 'D:\Songs'
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, random.choice(song)))
            print(os.path.join(music_dir, random.choice(song)))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir, the is {strTime}")

        elif 'the date' in query:
            strdate = datetime.datetime.now().strftime("%m/%d/%Y")
            print(strdate)
            speak(f"sir, the is {strdate}")

        elif 'open code' in query:
            codepath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        if 'exit' in query:
            exit()