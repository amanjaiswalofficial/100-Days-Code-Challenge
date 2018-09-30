from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts=gTTS(text=audio,lang='en')
    tts.save('audio.mp3')#saving the provided input as mp3
    os.system('mpg123 audio.mp3')#to play the audio

#listen to command
def myCommand():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Ready to roll")
        r.pause_threshold=1 #time before it starts listening for next one
        r.adjust_for_ambient_noise(source,duration=1) #to avoid background noise
        audio=r.listen(source)

    try:
        command=r.recognize_google(audio)#equal to command that was taken as input
        print("You said: "+str(command)+"\n")

    #loopback to continue to listen to command if something recognizable is found

    except sr.UnknownValueError:
        assistant(myCommand())
    
    return command

#if statements for executing commands
def assistant(command):
    if 'open facebook' in command:
        os.system('C:\Program Files\Mozilla Firefox\Firefox.exe -new-tab http://www.facebook.com/')
        """chrome_path='/usr/bin/google-chrome'
        url='https://www.reddit.com/r/python'
        webbrowser.get(chrome_path).open(url)"""
    
    if 'what\'s up' in command:
        talkToMe('Chillin bro')

talkToMe('I\'m ready for your command')

while True:
    assistant(myCommand())


    

print('All good')
