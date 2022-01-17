#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pyttsx3 as pt
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
# import PyAudio


# to open the microphone
listener = sr.Recognizer()
engine = pt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as source:
        print("Listening.........")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'bot' in command:
            command = command.replace('bot', '')
            print(command)
    return command


def run_bot():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I : %M %p')
        talk('Current Time is' + time)
    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'what' in command:
        person = command.replace('what', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('I am a robot in relationship with who talks to me')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'bye' in command:
        command = command.lower()
    else:
        talk('I am a Bot not God , Refer the internet or other sources')


while True:
    run_bot()


# In[ ]:





# In[ ]:




