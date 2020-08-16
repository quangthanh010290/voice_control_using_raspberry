#!/usr/bin/python3

import pyttsx3
import speech_recognition as sr
import pyaudio
from gpiozero import LED

for i, mic_name in enumerate (sr.Microphone.list_microphone_names()):
    print("mic: " + mic_name)
    if "USB Audio Devic" in mic_name:
        print("USB Audio Devic " + mic_name)
        mic = sr.Microphone(device_index=i, chunk_size=1024, sample_rate=48000)


pi_ear = sr.Recognizer()
pi_mouth = pyttsx3.init()
light_1 = LED(17)
fan = LED(27)
light_1.on()
fan.on()

while True:
    need_speak = False
    with mic as source:
        # pi_ear.pause_thpi_eareshold=1
        pi_ear.adjust_for_ambient_noise(source, duration=0.5)
        print("\033[0;35mpi: \033[0m I'm listening")
        audio = pi_ear.listen(source)
    try:
        you = pi_ear.recognize_google(audio)
    except:
        you = ""
    msg = you
    if you == "":
        msg="I can't hear you, please try again"
        need_speak = True
    elif "turn on light" in you:
        msg="sure, I'm turning on the light"
        light_1.off()
        need_speak = True
    elif "turn on fan" in you:
        msg="sure, I'm turning on the fan"
        fan.off()
        need_speak = True
    elif "turn on the light" in you:
        msg = "sure, I'm turning on the light"
        light_1.off()
        need_speak = True
    elif "turn off light" in you:
        msg = "sure, I'm turning off the light"
        light_1.on()
        need_speak = True
    elif "turn off fan" in you:
        msg = "sure, I'm turning off the fan"
        fan.on()
        need_speak = True
    elif "turn off the light" in you:
        msg="sure, I'm turning off the light"
        light_1.on()
        need_speak = True
    elif "bye" in you:
        msg="thank you"
        print("\033[0;32myou:\033[0m " + you)
        print("\033[0;35mpi:\033[0m " + msg)
        pi_mouth.say(msg)
        pi_mouth.runAndWait()
        break
    print("\033[0;32myou:\033[0m " + you)
    print("\033[0;35mpi:\033[0m " + msg)
    if need_speak == True:
        pi_mouth.say(msg)
        pi_mouth.runAndWait()
