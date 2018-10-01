import speech_recognition as sr
r=sr.Recognizer()

#r.recognize_google()
harvard=sr.AudioFile('harvard.wav')

#below is transcribing the first audio file, whatever that may mean

"""with harvard as source:
    audio=r.record(source)

print(r.recognize_google(audio))"""
#this is what it prints after testing the audio file


#doing the same thing for a set of seconds

"""with harvard as source:
    audio1 = r.record(source,duration=4)
    audio2=r.record(source,duration=4)
    
print(r.recognize_google(audio1))#first 4 seconds
print(r.recognize_google(audio2))#next 4 seconds"""


#to record only a specific part of the file, leaving the rest behind
with harvard as source:
    audio=r.record(source,offset=4,duration=3) #this skips the first 4 seconds and gets to the 2nd part

print(r.recognize_google(audio))

#working with background noises

#here jackhammer is a file with noise, not downloaded yet
"""with jackhammer as source:
    r.adjust_for_ambient_noise(source,duration=0.5)#this uses a method to avoid background noises
    audio=r.record(source)

print(r.recognize_google(audio))"""

#to print the possible alternatives for any recognized speech
print(r.recognize_google(audio, show_all=True)) #this shows all possible alternatives