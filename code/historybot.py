# John Harney, Centre College, updated 10.21.19

# this code exists thanks to Texas-Mark on the official RPi forums,
# he shared the code the original (PIR sensor) iteration of this was based on at
# https://www.raspberrypi.org/forums/viewtopic.php?t=176241

# button code version relied heavily on Soren at
# https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

# this is the base code for all history bots as of 10.21.19

import RPi.GPIO as GPIO
import time
import os
import random

GPIO.setmode(GPIO.BCM) # use the GPIO numbering
GPIO.setwarnings(False) # Avoids warning channel is already in use

led = 21 # GPIO pin 21
button = 18 # GPIO pin 18
button_led = 26 # GPIO pin 26

GPIO.setup(led,GPIO.OUT) # sets up pin 21 to output
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) #sets up pin 18 as a button
GPIO.setup(button_led,GPIO.OUT) #sets up pin 26 to output

# maybe change the next few lines to a function, not sure

l_dirlist = os.listdir()
l_audiofiles = []

# following code works only with mp3s and if you are using mpg123;
# I need to check if this solution works on RPi, and it would be nice
# to support mp3s and wav files

for file in l_dirlist:
    if file[-4:] == ".mp3":
        #l_audiofiles.append("'omxplayer -o alsa "  + file + "'")
        #l_audiofiles.append("'mpg123 "  + file + "'")
        l_audiofiles.append("mpg123 "  + file)
# os.system(random.choice(l_audiofiles))

# this counter is used to make sure the notification uses correct grammar
i_count = 0

# following code is where the magic happens

while True:
        GPIO.output(button_led, True) # turn on button led
        input_state = GPIO.input(button) # primes the button!
        if input_state == False:
            i_count = i_count + 1
            GPIO.output(button_led, False) # turns off button led
            GPIO.output(led,True) #Turn on LED
            #os.system(random.choice(myList)) # play sound file
            os.system(random.choice(l_audiofiles))
            GPIO.output(led,False) #turn off LED
            if i_count == 1:
                print("History Bot has been activated " + str(i_count) + " time!")
            else:
                print("History Bot has been activated " + str(i_count) + " times!")
            GPIO.output(button_led, True) # turns button led back on
            time.sleep(0.2)
