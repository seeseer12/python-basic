import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# initialize text to speech
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning Sir")
    elif hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am Jarvis. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception:
        speak("Sorry, please say that again")
        return "none"
    return query.lower()

# main program
wish_me()

while True:
    query = take_command()

    if 'wikipedia' in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(result)

    elif 'open google' in query:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif 'open youtube' in query:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif 'time' in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")

    elif 'open vscode' in query:
        os.startfile("C:\\Users\\YourUser\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif 'exit' in query or 'quit' in query:
        speak("Goodbye Sir")
        break
