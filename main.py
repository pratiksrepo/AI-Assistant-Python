import datetime
import os
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

import openai
from Apikey import key

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

chatStr = ""


def chat(query):
    global chatStr

    openai.api_key = key
    chatStr += f"Pratik:{query}\n Sara:"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        speak(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]

    except Exception as e:
        print(e)

    if not os.path.exists("openai"):
        os.mkdir("Openai")

    with open(f"openai/{''.join(query.split('ai')[1:])}.txt", "w") as f:
        f.write(chatStr)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishmee():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak("Hello sir i am sara here what may i help u")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


def sendEmail(to, content):
    pass


def ai(prompt):
    openai.api_key = key
    text = f"OpenAi Response for Prompt:{prompt}\n*******************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        print(response["choices"][0]["text"])
        text += response["choices"][0]["text"]

    except Exception as e:
        print(e)

    if not os.path.exists("openai"):
        os.mkdir("Openai")

    with open(f"openai/{''.join(prompt.split('ai')[1:])}.txt", "w") as f:
        f.write(text)


if __name__ == '__main__':
    wishmee()

    while True:

        # if=1:
        query = takeCommand().lower()  # Converting user query into lower case

        if 'wikipedia' in query:
            speak('searching Wikipedia..')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open browser' in query:
            webbrowser.open('https://google.com')
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')


        elif 'play music' in query:
            music_dir = "D:\\Python\\jarvis"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what time it is' in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak(f"Sir,the time is{hour} bajke {min} minutes")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\prati\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)



        elif "Using AI ".lower() in query.lower():
            ai(prompt=query)

        elif "Sara Stop it".lower() in query.lower():
            exit()

        elif "Sara Reset Chat".lower() in query.lower():
            chatStr = ""

        else:
            chat(query)
            print("chatting...", chatStr)
