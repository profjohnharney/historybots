# John Harney, Centre College, updated 08.04.2020

# initial writing of the button code relied on:
# Texas-Mark on the official RPi forums: https://www.raspberrypi.org/forums/viewtopic.php?t=176241
# and
# Soren at https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

import RPi.GPIO as GPIO
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

# code takes all mp3 and wav files in the SAME directory as the script
# and queues them up for the random function below

path = "./" # this is being added so that the script works in Python 2.7
l_dirlist = os.listdir(path) # Python 2.7 requires an argument; argument is optional in Python 3
l_audiofiles = []
for file in l_dirlist:
    if file[-4:] == ".mp3" or file[-4:] == ".wav":
        l_audiofiles.append("omxplayer -o alsa "  + file)
    
i_count = 0 # this counter is used so notifications use correct grammar

# following code is where the magic happens

while True: # sets this code on a loop
        GPIO.output(button_led, True) # turn on button led
        input_state = GPIO.input(button) # primes the button!
        playList = l_audiofiles # gets the list ready to avoid repitition of tracks
        if input_state == False: # False == button press
            i_count = i_count + 1 
            GPIO.output(button_led, False) # turns off button led
            GPIO.output(led,True) #Turn on LED
            playfile = random.choice(l_audiofiles) # selects an audio file from the directory
            while playfile == playList[-1] or playfile == playList[-2]: # checks to make sure file was not one of last two played
                playfile = random.choice(l_audiofiles)
            os.system(playfile) # plays file via command line
            playList.append(playfile) # adds played file to playlist to avoid repetition
            GPIO.output(led,False) #turn off LED
            if i_count == 1:
                print("History Bot has been activated!")
            else:
                print("History Bot has been activated " + str(i_count) + " times!")
            GPIO.output(button_led, True) # turns button led back on
