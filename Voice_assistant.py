import speech_recognition as sr   
import pyttsx3  
import pyaudio as p
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening..')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
                # talk(command)
    except Exception:
    	print("Hello")
    return command
def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing '+song)
        pywhatkit.playonyt(song)
        print(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is '+time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry i have a boyfriend')
    elif 'single' in command:
        talk('sorry i am in relationship')
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'name' or 'naam' in command:
        talk('kaa haal baa thora gau konsa jeela konsa')
        talk('mai aapki kya sahayta kar sakti huu')
    elif 'google' in command:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in command:
    	webbrowser.open("stackoverflow.com")   
    else:
        talk('please say the command again')
while True:
        run_alexa()