from playsound import playsound
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import socket
from time import sleep, time
import time
import sys
import pyjokes
import pyautogui
import smtplib
from requests import get
import pyaudio
from keyboard import press
from keyboard import press_and_release
from keyboard import write


number_list = [0, 1, 2]

rand = random.choice(number_list)
random = int(rand)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak('I am ONLINE')
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Night Sir")

    speak("Hello Sir. I am jarvis. Your Assistant. How Can I help u Sir ")
    speak("I can Do the following things : -")
    f = open("info.txt", "r")
    print(f.read())
    time.sleep(1.5)


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        #speak("Sir anything for me")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said:: {query}\n")
    except Exception as e:
        print("Me::Sir Please Say again.....")

        return "None"

    return query


def wait():
    print("\nWaiting ", end="")
    list1 = [".", ".", ".", ".", ".", ".", ".", "."]
    for i in (list1):
        print(f"{i}", end="")
        time.sleep(1)


def screen():
    img = pyautogui.screenshot()
    img.save("screenshot_1.png")


def jokes():
    speak(pyjokes.get_joke())


def check_internet():

    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        s.close()
        speak("Please Wait Sir ....\n I am checking your internet connection...")
        wait()
        speak("Your Internet is Working Sir")
    except Exception as e:
        speak("Please Wait Sir ....\n I am checking your internet connection...")
        wait()
        speak("Your Internet connection is down Sir...But i am still Checking....")
        sys.exit()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching on Wikipedia .... please wait Sir...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia Sir")
            print(f"\n Result is :{result}")
            speak(result)
            speak("Task Complete \n Any thing for me Sir")

        elif 'youtube' in query:
            speak("openning youtube")
            webbrowser.open("youtube.com")

        elif 'check internet' in query:
            check_internet()

        elif 'hello jarvis' in query:
            speak('Hello Sir')

        elif 'jokes' in query:
            jokes()

        elif 'screen' in query:
            speak("Sir i take a screenshot")
            screen()

        elif 'play music' in query:
            speak("Playing music For you Sir")
            playsound("Music.wav")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Kavya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("Task Complete \n Any thing for me Sir")

        elif 'who are you' in query:
            speak("I am jarvis. Your Assistant and Also Your Friend . Just A Rather Very Intelligent System. I can Any thing for you")

        elif 'yes jarvis' in query:
            speak("Ok Sir")

        elif 'no jarvis' in query:
            speak("Can i go OFFLINE Sir")
            cmd = takeCommand().lower()
            if cmd == "yes":
                speak("I am going OFFLINE sir")
                speak("jarvis out")
                break
                sys.exit()

            elif cmd == "no":
                speak('Ok Sir . I am With u')
            else:
                speak("i cannot Understand Sir")

        elif 'search' in query:
            speak("opening Google")
            webbrowser.open("google.com")
            speak("Task done...... Any thing for me Sir")

        elif 'log out' in query:
            speak("Sir system is logging out")
            speak("Sir Goodbye")
            os.system("shutdown -l")

        elif 'shut down' in query:
            speak("Sir system is Shuting down")
            speak("Goodbye Sir ")
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            speak("Sir system is Restarting")
            speak("Goodbye Sir ")
            os.system("shutdown /r /t 1")

        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
            speak("Sir i am Remembering Your Data")
            speak("Any thing for me Sir")

        elif 'do you know anything' in query:
            speak("Yes Sir")
            remember = open('data.txt', 'r')
            speak("You said me to remember that" + remember.read())

        elif 'online' in query:
            speak('Yess I am ONLINE Sir')
            speak("Any thing for me Sir")

        elif 'mail' in query:
            speak("Opening mail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'search in chrome' in query:
            speak("What should i search ?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            webbrowser.get(chromepath).open_new_tab(search+'.com')
            speak('task complete.......  Any thing For me Sir')

        elif 'offline' in query:
            speak('Going to OFFLINE Sir.... Good Bye Sir')
            speak('Jarvis Outtt')
            break
            sys.exit()

        elif 'notepad' in query:
            speak("openning Notepad")
            path = ("C:\\Windows\\system32\\notepad.exe")
            os.startfile(path)
            speak("task Done Sir")

        elif 'cmd' in query:
            speak("openning Command and prompt")
            os.system("start cmd")

        elif 'calculator' in query:
            path = ("C:\\Windows\\system32\\calc.exe")
            os.startfile(path)
            speak("Task Done Sir")

        elif 'ip' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Sir your ip address is {ip}")
            print(f"Sir your ip address is {ip}")

        elif 'open stack overflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("www.stackoverflow.com")

        elif 'open w3school' in query:
            speak("opening w3schools")
            webbrowser.open("www.w3schools.com")

        elif 'Git Hub' in query:
            speak("opening github")
            webbrowser.open("www.github.com")
            speak("Task Complete \n Any thing for me Sir")

        elif 'find on google' in query:
            speak("Sir, What should i search on google")
            com = takeCommand().lower()
            webbrowser.open(f"{com}")
            speak("Task Complete \n Any thing for me Sir")

        elif 'bye' in query:
            speak("bye bye sir,you can call me anytime")
            break

        elif 'get lost' in query:
            sys.exit()

        else:
            speak("Sorry Sir I cannot understand ........   What i do ???")