from tkinter import *
import PIL.Image, PIL.ImageTk
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import random
import pyjokes
import randfacts
import random
import wikipedia
import requests
import json
from difflib import get_close_matches
from news import *
from bs4 import BeautifulSoup

numbers = {'hundred':100, 'thousand':1000, 'lakh':100000}
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query

def play():
    btn2['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    while True:
        btn1.configure(bg = 'orange')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("goodbye")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            window.update()
            speak("goodbye")
            break

        elif 'hello' in query:
            greetings = ["hey, how can I help you", "what's up?", "I'm listening"]
            greet = greetings[random.randint(0,len(greetings)-1)]
            var.set(greet)
            speak(greet)

        elif "name" in query:
            var.set('my name is Autumn.')
            speak("my name is Autumn.")
        
        elif "how are you" in query:
            var.set("I'm very well, thanks for asking")
            speak("I'm very well, thanks for asking")

        elif 'what can you do' in query:
            var.set('I can tell the time, start a conversation, joke, open youtube, search google, calculate and many other things')
            window.update()
            speak('I can tell the time, start a conversation, joke, open youtube, search google, calculate and many other things')

        elif "time" in query:
            digi_time = datetime.datetime.now().strftime('%I %M %p')
            var.set(f'the time is {digi_time}')
            speak(f'the time is {digi_time}')

        elif "youtube" in query:
            search_term = query.split("for")[-1]
            url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.get().open(url)
            var.set(f'Here is what I found for {search_term}')
            speak(f'Here is what I found for {search_term}')
            
        elif "joke" in query:
            My_joke = pyjokes.get_joke()
            var.set(My_joke)
            speak(My_joke)

        elif "what" in query and "youtube" not in query and 'name' not in query and 'can you do' not in query and 'meaning' not in query:
            search_term = query
            url = f"https://www.google.com/search?q={search_term}"
            webbrowser.get().open(url)
            search_term = query.split("what is")[-1]
            speak(f"this is what i found for {search_term} on google")

        elif "who" in query and "youtube" not in query:
            search_term = query
            url = f"https://www.google.com/search?q={search_term}"
            webbrowser.get().open(url)
            search_term = query.split("who is")[-1]
            speak(f"this is what i found for {search_term} on google")

        elif "which" in query and "youtube" not in query:
            search_term = query
            url = f"https://www.google.com/search?q={search_term}"
            webbrowser.get().open(url)
            speak(f"this is what i found for {search_term} on google")

        elif "how" in query and "youtube" not in query:
            search_term = query
            url = f"https://www.google.com/search?q={search_term}"
            webbrowser.get().open(url)
            speak(f"this is what i found for {search_term} on google")

        elif "calculate" in query:
            voice_data = speak('what do you want me to calculate')
            voice_data = takeCommand()
            res = [int(i) for i in voice_data.split() if i.isdigit()]
            n1 = int(res[0])
            n2 = int(res[1])
            if 'ad' in voice_data or '+' in voice_data or 'plus' in voice_data:
                n = n1 + n2
                var.set(f'the answer is {n}')
                speak(f'the answer is {n}')
            if 'subtract' in voice_data or 'minus' in voice_data or '-' in voice_data:
                n = n1 - n2
                var.set(f'the answer is {n}')
                speak(f'the answer is {n}')
            if 'divided by' in voice_data or '/' in voice_data:
                n = n1 / n2
                var.set(f'the answer is {n}')
                speak(f'the answer is {n}')
            if 'multiply' in voice_data or 'into' in voice_data or 'x' in voice_data or '*' in voice_data:
                n = n1 * n2
                var.set(f'the answer is {n}')
                speak(f'the answer is {n}')

        elif "fact" in query:
            fact = randfacts.get_fact()
            var.set(f'Did you know that {fact}')
            speak(f'Did you know that {fact}')  

        elif "random" in query:
            rand = random.randint(1, 6)
            var.set("the number is {}".format(rand))
            speak("the number is {}".format(rand))

        elif "roll a die" in query:
            rand = random.randint(1, 6)
            var.set("the number is {}".format(rand))
            speak("the number is {}".format(rand))

        elif "flip a coin" in query:
            coin = ['heads'] * 50 + ['tails'] * 50 + ['perpendicular'] * 1
            var.set(random.choice(coin))
            speak(random.choice(coin))

        elif "location" in query:
            location = speak('Which location you want to search for')
            location = takeCommand()
            url = 'https://www.google.nl/maps/place/' + str(location)
            webbrowser.get().open(url)
            var.set("this is " + str(location))
            speak("this is " + str(location))

        elif "wiki" in query:
            var.set('what do you want to search for')
            answer = speak('what do you want to search for')
            answer = takeCommand()
            var.set('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            speak(wikipedia.summary(answer, sentences=2))

        elif "wikipedia" in query:
            var.set('what do you want to search for')
            answer = speak('what do you want to search for')
            answer = takeCommand()
            var.set('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            speak(wikipedia.summary(answer, sentences=2))

        elif "viki" in query:
            var.set('what do you want to search for')
            answer = speak('what do you want to search for')
            answer = takeCommand()
            var.set('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            speak(wikipedia.summary(answer, sentences=2))

        elif "vikipedia" in query:
            var.set('what do you want to search for')
            answer = speak('what do you want to search for')
            answer = takeCommand()
            var.set('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            speak(wikipedia.summary(answer, sentences=2))

        elif 'weather' in query:
            var.set('searching for the data..')
            speak('searching for the data..')
            url = 'https://www.google.co.in/search?q=weather+in+bangalore+today'
            webbrowser.get().open(url)
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            weather_forecast = data.find("div", class_="BNeawe").text
            speak(f'the weather forecast is as shown. The temperature is {weather_forecast}')

        elif 'meaning' in query:
            #load JSON data
            data = json.load(open("data.json"))

            word = speak('what is the word')
            word = takeCommand()

            def getMeaning(w):
                w = w.lower()
                if w in data:
                    return data[w]
                elif len(get_close_matches(w,data.keys())) > 0:
                    close_match = get_close_matches(w,data.keys())[0]
                    choice = speak("Did you mean %s instead? say yes or no" % close_match)
                    choice = takeCommand()
                    choice = choice.lower()
                    if choice == 'yes':
                        speak(data[close_match])
                    elif choice == 'no':
                        speak('The word doesnt exist. Please double check it.')
                    else:
                        speak('Sorry, We didnt understand your entry.')
                else:
                    speak("The word doesn't exist. Please double check it.")

            meaning = getMeaning(word)
            #speaking meaning of the word in console
            if type(meaning) == list:
                for item in meaning:
                    speak(item)
            else:
                speak(meaning)

        elif 'news' in query:
            var.set('Ok i will speak the news now')
            speak('Ok i will speak the news now')
            arr = news()
            for i in range(len(arr)):
                speak(arr[i])

        elif 'good morning' in query:
            # wish me main
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                search_term = "temperature in bangalore"
                url = f"https://www.google.com/search?q={search_term}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                time = datetime.datetime.now().strftime('%I %M %p')
                var.set('Good morning,this is Autumn')
                speak('Good morning,this is Autumn')
                var.set('the time is ' + time)
                speak('the time is ' + time)
                var.set(f'the current {search_term} is {temp}')
                speak(f'the current {search_term} is {temp}')
                var.set('importing system data, all functions operational, im here when you need me.')
                speak('importing system data, all functions operational, im here when you need me.')
            if hour >= 12 and hour < 18:
                search_term = "temperature in bangalore"
                url = f"https://www.google.com/search?q={search_term}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                time = datetime.datetime.now().strftime('%I %M %p')
                var.set('Good afternoon,this is Autumn')
                speak('Good afternoon,this is Autumn')
                var.set(f'the current time is {time}')
                speak(f'the current time is {time}')
                var.set(f'the current {search_term} is {temp}')
                speak(f'the current {search_term} is {temp}')
                var.set('importing system data... all functions operational')
                speak('importing system data... all functions operational')

        elif 'good evening' in query:
            # wish me main
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                search_term = "temperature in bangalore"
                url = f"https://www.google.com/search?q={search_term}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                time = datetime.datetime.now().strftime('%I %M %p')
                var.set('Good morning,this is Autumn')
                speak('Good morning,this is Autumn')
                var.set('the time is ' + time)
                speak('the time is ' + time)
                var.set(f'the current {search_term} is {temp}')
                speak(f'the current {search_term} is {temp}')
                var.set('importing system data, all functions operational, im here when you need me.')
                speak('importing system data, all functions operational, im here when you need me.')
            if hour >= 12 and hour < 18:
                search_term = "temperature in bangalore"
                url = f"https://www.google.com/search?q={search_term}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                time = datetime.datetime.now().strftime('%I %M %p')
                var.set('Good afternoon,this is Autumn')
                speak('Good afternoon,this is Autumn')
                var.set(f'the current time is {time}')
                speak(f'the current time is {time}')
                var.set(f'the current {search_term} is {temp}')
                speak(f'the current {search_term} is {temp}')
                var.set('importing system data... all functions operational')
                speak('importing system data... all functions operational')

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('Autumn')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()
window['bg']='black'

window.mainloop()