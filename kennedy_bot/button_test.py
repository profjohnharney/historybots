# this code exists thanks to Texas-Mark on the official RPi forums, 
# he shared the code the original iteration of this was (heavily) based on at 
# https://www.raspberrypi.org/forums/viewtopic.php?t=176241

import RPi.GPIO as GPIO
import time
import os
import random


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pir_sensor = 4 #GPIO pin 4
led = 21 #GPIO pin 21
myCmd1 = 'omxplayer -o alsa kennedy1.mp3'
myCmd2 = 'omxplayer -o alsa kennedy2.mp3'
myCmd3 = 'omxplayer -o alsa kennedy3.mp3'
myCmd4 = 'omxplayer -o alsa kennedy4.mp3'
myList = [myCmd1, myCmd2, myCmd3, myCmd4]

GPIO.setup(pir_sensor, GPIO.IN, GPIO.PUD_DOWN)

current_state = 0
GPIO.setup(led,GPIO.OUT)

while True:
    try:
        time.sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
          GPIO.output(led,True) #Turn on LED
          os.system(random.choice(myList)) # plays one of the mp3 files
          GPIO.output(led,False) #turn off LED
          time.sleep(4) # wait 4 seconds for PIR to reset.
    except KeyboardInterrupt:
        GPIO.cleanup()
