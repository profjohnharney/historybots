# John Harney, Centre College, updated 05.19.20

# writing of the button code relied on:
# Texas-Mark on the official RPi forums: https://www.raspberrypi.org/forums/viewtopic.php?t=176241
# and
# Soren at https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

# this is the "Yeats_bot", a history bot based on William Butler Yeats
# this is an example of how to write a bot using text-to-speech

# this code is based on the idea you will place (theoretically short)
# plaint text files in the same directory as the script

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

# maybe change the next few lines to a function, not sure

l_dirlist = os.listdir()
l_textfiles = []

# code takes text files in the SAME directory as the script
# and plays the audio through the USB speaker
# USB audio on RPi can be finicky; if you are having trouble consult
# https://www.raspberrypi-spy.co.uk/2019/06/using-a-usb-audio-device-with-the-raspberry-pi/

for file in l_dirlist:
        l_textfiles.append("espeak --stdout " + file + " | aplay")

i_count = 0 # this counter is used so notification uses correct grammar

# following code is where the magic happens

while True: # sets this code on a loop
        GPIO.output(button_led, True) # turn on button led
        input_state = GPIO.input(button) # primes the button!
        if input_state == False: # False == button press
            i_count = i_count + 1
            GPIO.output(button_led, False) # turns off button led
            GPIO.output(led,True) #Turn on LED
            os.system(random.choice(l_textfiles)) # takes random file from list and plays through command line
            GPIO.output(led,False) #turn off LED
            if i_count == 1:
                print("History Bot has been activated!")
            else:
                print("History Bot has been activated " + str(i_count) + " times!")
            GPIO.output(button_led, True) # turns button led back on
            time.sleep(0.2) # brief delay to keep the loop working
