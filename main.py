# Python TextToSpeech Library
import speech_recognition as sr

# Decouple is used to read .env file
from decouple import config
from datetime import datetime
from random import choice
# Our custom file containing a list of sentences
from utils import opening_text

# Import our functions
from functions.speak import speak
from functions.online_ops import find_my_ip, search_wikipedia, play_on_youtube, search_on_google, send_whatsapp_msg, send_email
from functions.os_ops import open_calculator, open_camera, open_cmd
from functions.gen_ops import talk_back


USERNAME = config('USER')
BOTNAME  = config('BOTNAME')


def greet_user():
    """Greets the user according to the time"""

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good Afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")

def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-us')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 12 and hour < 6:
                speak("Good Night and Take Care!")
            else:
                speak("Have a Good Day!")
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open calculator' in query or 'open calc' in query:
            open_calculator()
        
        elif 'open cmd' in query or 'open command prompt' in query:
            open_cmd()
        
        elif 'open camera' in query:
            open_camera()
        
        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia?')
            search_query = take_user_input().lower()
            results = search_wikipedia(query)
            speak(f'According to Wikipedia, {results}')
            speak(f'For your convenience, I am printing it on the screen')
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on YouTube?')
            video_keyword = take_user_input().lower()
            play_on_youtube(video_keyword)
        
        elif 'search on google' in query or 'google something' in query:
            speak('What do you want to search on Google?')
            query = take_user_input().lower()
            search_on_google(query)
        
        elif 'greet someone' in query:
            speak('Who do you want to greet?')
            name = take_user_input().lower()
            speak(f'Hi, {name}, how are you today?')
        
        elif 'say your name' in query:
            speak(f'My name is {BOTNAME}')

        # else:
        #     talk_back()
