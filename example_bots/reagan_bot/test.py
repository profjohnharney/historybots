# John Harney, Centre College, updated 08.03.2020
# THIS IS A TEST

# writing of the button code relied on:
# Texas-Mark on the official RPi forums: https://www.raspberrypi.org/forums/viewtopic.php?t=176241
# and
# Soren at https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

import RPi.GPIO as GPIO
import time # for sleep function below
import os # for commands via console
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # Avoids warning channel is already in use

led = 21
button = 18
button_led = 26

GPIO.setup(led,GPIO.OUT) # sets up pin 21 as led
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) # sets up pin 18 as a button
GPIO.setup(button_led,GPIO.OUT) # sets up pin 26 to output

path = "./" # this is being added so that the script works in Python 2.7
l_dirlist = os.listdir(path) # Python 2.7 requires an argument; optional in Python 3
l_audiofiles = []

# code takes all mp3 and wav files in the SAME directory as the script
# and queues them up for the random function below

for file in l_dirlist:
    if file[-4:] == ".mp3" or file[-4:] == ".wav":
        l_audiofiles.append("omxplayer -o alsa "  + file)

# this function ensures the same file is not played twice in a row 
# this does not actually work.... rather than play the same sound twice it will just go back to wait to be activated, having done nothing

# def playFile():
#     playList = []
#     playfile = random.choice(l_audiofiles)
#     while playfile == playList[-1]:
#         playfile = random.choice(l_audiofiles)
#     os.system(playfile)
#     playList.append(playfile)
    
i_count = 0 # this counter is used so notification uses correct grammar

# following code is where the magic happens

while True: # sets this code on a loop
        GPIO.output(button_led, True) # turn on button led
        input_state = GPIO.input(button) # primes the button!
        playList = l_audiofiles # gets the list ready to avoid repitition of tracks
        if input_state == False: # False == button press
            i_count = i_count + 1
            GPIO.output(button_led, False) # turns off button led
            GPIO.output(led,True) #Turn on LED
            playfile = random.choice(l_audiofiles)
            while playfile == playList[-1]:
                playfile = random.choice(l_audiofiles)
            os.system(playfile)
            playList.append(playfile)
            #os.system(random.choice(l_audiofiles)) # takes random file from list and plays through command line
            GPIO.output(led,False) #turn off LED
            if i_count == 1:
                print("History Bot has been activated!")
            else:
                print("History Bot has been activated " + str(i_count) + " times!")
	    print(playList)
	    GPIO.output(button_led, True) # turns button led back on
        time.sleep(0.2) # brief delay to keep the loop working
