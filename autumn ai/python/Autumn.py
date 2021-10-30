import speech_recognition as sr 
import playsound 
from gtts import gTTS
import pyttsx3
import random
import webbrowser
import time
import os # to remove created audio files
import pywhatkit
import pyjokes
import requests
from bs4 import BeautifulSoup
from news import *
import randfacts
import datetime
import requests
import wikipedia
import json
from difflib import get_close_matches
from googletrans import Translator, constants

class person:
    name = ''
    def setName(self, name):
        self.name = name
def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True
r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:

def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        r.adjust_for_ambient_noise(source) #it makes it to recognize much clearly, by reducing background noise
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            speak('please repeat')
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
# setting up sound engine, for fast response (reply)
try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1)
    engine.setProperty('voices', voices[0].id)
except Exception as e:
    print(e)
    quit()

#playing output audio
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"Autumn: {audio_string}") # print what app said
    os.remove(audio_file) # remove audio file
    engine.runAndWait()

def respond(voice_data):

    # 1: wishme
    if there_exists(['good morning', 'good evening']):
        
        # wish me main
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            search_term = "temperature in bangalore"
            url = f"https://www.google.com/search?q={search_term}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            time = datetime.datetime.now().strftime('%I %M %p')
            speak('Good morning,this is Autumn')
            speak('the time is ' + time)
            speak(f'the current {search_term} is {temp}')
            speak('importing system data, all functions operational, im here when you need me.')
        if hour >= 12 and hour < 18:
            search_term = "temperature in bangalore"
            url = f"https://www.google.com/search?q={search_term}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            time = datetime.datetime.now().strftime('%I %M %p')
            speak('Good afternoon,this is Autumn')
            speak('the current time is {time}')
            speak(f'the current {search_term} is {temp}')
            speak('importing system data... all functions operational')

    # 2: greeting
    elif there_exists(['hey','hi','hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    # 3: name
    elif there_exists(["what is your name","what's your name","tell me your name", "who are you"]):
        if person_obj.name:
            speak("my name is Autumn")
        else:
            speak("my name is Autumn. what's your name?")
    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        speak("okay, i will remember that name")
        person_obj.setName(person_name) # remember name in person object

    # 4: greeting
    elif there_exists(["how are you","how are you doing"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}")

    # 5: time
    elif there_exists(["time"]):
        digi_time = datetime.datetime.now().strftime('%I %M %p')
        speak(f'the time is {digi_time}')

    # 6: search youtube
    elif there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')
    
    # 7: play song
    elif there_exists(["play"]):
        command = voice_data.split("play")[-1]
        pywhatkit.playonyt(command)
    
    # 8: jokes
    elif there_exists(['joke', 'jokes']):
        My_joke = pyjokes.get_joke()
        speak(My_joke)

    # 9: search google
    elif there_exists(["what", 'who', 'how', 'which']) and 'youtube' not in voice_data:
        search_term = voice_data
        url = f"https://www.google.com/search?q={search_term}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        google_search = data.find("div", class_="BNeawe").text
        speak(f"Here is what i found for {search_term} on google")
        speak(f"{google_search}")

    # 10: calculation / math
    elif there_exists(['calculate', 'calculation']):
        voice_data = speak('what do you want me to calculate')
        voice_data = record_audio()
        res = [int(i) for i in voice_data.split() if i.isdigit()]
        n1 = int(res[0])
        n2 = int(res[1])
        if 'add' in voice_data or 'ad' in voice_data or 'plus' in voice_data:
            n = n1 + n2
            speak(f'the answer is {n}')
        if 'subtract' in voice_data or 'minus' in voice_data:
            n = n1 - n2
            speak(f'the answer is {n}')
        if 'divided by' in voice_data:
            n = n1 / n2
            speak(f'the answer is {n}')
        if 'multiply' in voice_data or 'into' in voice_data:
            n = n1 * n2
            speak(f'the answer is {n}')

    # 11: news
    elif there_exists(['news']):
        speak('Ok i will speak the news now')
        arr = news()
        for i in range(len(arr)):
            speak(arr[i])
    
    # 12: facts
    elif there_exists(['fact', 'facts']):
        fact = randfacts.getFact()
        speak(f'Did you know that {fact}')   

    # 13: random number
    elif there_exists(["roll a die", "random"]):
        rand = random.randint(1, 6)
        speak("Result is {}".format(rand))

    # 14: flip a coin
    elif there_exists(["flip a coin"]):
        coin = ['heads'] * 50 + ['tails'] * 50 + ['perpendicular'] * 1
        speak(random.choice(coin))

    # 15: translate
    elif there_exists(["translate"]):
        sentence = speak('Which word or sentence do you want to translate')
        sentence = record_audio()
        language = speak('which language do you want to translate to')
        language = record_audio()

        if language == 'bengali':
            language = 'bn'
        if language == 'chinese':
            language = 'zh-cn'
        if language == 'chinese':
            language = 'zh-cn'
        if language == 'french':
            language = 'fr'
        if language == 'german':
            language = 'de'
        if language == 'hawaiian':
            language = 'haw'
        if language == 'italian':
            language = 'it'
        if language == 'japanese':
            language = 'ja'
        if language == 'hindi':
            language = 'hi'

        translator = Translator()
        translations = translator.translate([sentence], dest=language)
        for translation in translations:
            speak(f'the translation is {translation.text}')

    # 16: location
    elif there_exists(["find location", "location"]):
        location = speak('Which location you want to search for')
        location = record_audio()
        url = 'https://www.google.nl/maps/place/' + str(location)
        webbrowser.get().open(url)
        speak("here is your location" + str(location))

    # 17: wikipedia
    elif there_exists(["search on viki", "wikipedia", "search on wikipedia", "vikipedia"]):
        wiki = speak('what do you want to search for')
        wiki = record_audio()
        speak('Searching Wikipedia...')
        results = wikipedia.summary(wiki, sentences=2)
        speak("According to Wikipedia")
        speak(results)

    # 18: weather advanced
    elif there_exists(['what is the weather', 'weather', 'forecast', 'temperature', 'weather forecast']):
        city = speak('name of the city')
        city = record_audio()
        url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={61991750a4508faec7fd87347a51adcd}'.format(city)
        res = requests.get(url)
        data = res.json()
        temp = data['main']['temp']
        wind_speed = data['wind']['speed']
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        description = data['weather'][0]['description']

        speak('Temperature : {} degree celcius'.format(temp))
        speak('Wind Speed : {} m/s'.format(wind_speed))
        speak('Latitude : {}'.format(latitude))
        speak('Longitude : {}'.format(longitude))
        speak('Description : {}'.format(description))

    # 19: dictionary
    elif there_exists(['meaning', 'synonym']):
        #load JSON data
        data = json.load(open("data.json"))

        word = speak('what is the word')
        word = record_audio()

        def getMeaning(w):
            w = w.lower()
            if w in data:
                return data[w]
            elif len(get_close_matches(w,data.keys())) > 0:
                close_match = get_close_matches(w,data.keys())[0]
                choice = speak("Did you mean %s instead? say Y if yes or N if no: " % close_match)
                choice = record_audio()
                choice = choice.lower()
                if choice == 'y':
                    speak(data[close_match])
                elif choice == 'n':
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

    # 20: quit
    elif there_exists(["quit", "goodbye", "bye", "go to sleep", 'exit']):
        speak("goodbye, going offline")
        exit()

time.sleep(0.5)
person_obj = person()
while(0.5):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond