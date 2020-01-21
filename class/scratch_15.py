import RPi.GPIO as GPIO
import time
from time import sleep
import os
import random
import multiprocessing

GPIO.setmode(GPIO.BOARD) #use the GPIO numbering
GPIO.setwarnings(False) # Avoids warning channel is already in use

button = 18 # GPIO pin 18
button_led = 26 # GPIO pin 26

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #sets up pin 18 as a button
GPIO.setup(26,GPIO.OUT) #sets up pin 26 to output
GPIO.setup(11, GPIO.OUT)
pwm=GPIO.PWM(11, 50)

#espeak audio is purposely misspelled to make voice more lifelike

myCmd1 = ('espeak --stdout "Jeffery Epsteen did not kill himself" | aplay')
myCmd2 = ('espeak --stdout "It does not take many words to tell the truth" | aplay')
myCmd3 = ('espeak --stdout "Inside of me there are two dogs. One is mean and evil and the other is good and they fight each other all the time. When asked which one wins, I answer, the one I feed the most." | aplay')
myCmd4 = ('espeak --stdout "In myyy early days, I was eager to learn, and to do things, and therefore, I learned quickly." | aplay')
myCmd5 = ('espeak --stdout "The white man knows how to make everything, but he does not know how to distribute it." | aplay')
myCmd6 = ('espeak --stdout "As individual fingers, we can easily be broken, but all together we make a mighty fist." | aplay')
myCmd7 = ('espeak --stdout "You think I am a fool, but you are a greater fool, than I am." | aplay')
myCmd8 = ('espeak --stdout "The life my people want is a life of freedom. I have seen nothing that a white man has, houses or railways, clothing or food, that is as good as the right to move in the open country and live in our fashion." | aplay')
myCmd9 = ('espeak --stdout "I wish it to be remembered that I was the last man of my tribe to surrender my rifle." | aplay')

List = [myCmd1, myCmd2, myCmd3, myCmd4, myCmd5, myCmd6, myCmd7, myCmd8, myCmd9]

def servo_control():
        # This is where the arm code starts. Will run correctly 1st time, but only the 1st time
        pwm.start(0)

        pwm.ChangeDutyCycle(5) # left -90 deg position
        sleep(.25)

        pwm.ChangeDutyCycle(10) # right +90 deg position
        sleep(.25)

        pwm.ChangeDutyCycle(5) # left -90 deg position
        sleep(.25)

        pwm.ChangeDutyCycle(10) # right +90 deg position
        sleep(.25)

        pwm.ChangeDutyCycle(5) # left -90 deg position
        sleep(.25)

        pwm.ChangeDutyCycle(10) # right +90 deg position
        sleep(.25)

        pwm.ChangeDutyCycle(5) # left -90 deg position
        sleep(.25)

        pwm.ChangeDutyCycle(10) # right +90 deg position
        sleep(.25)

        pwm.ChangeDutyCycle(5) # left -90 deg position
        sleep(.25)

        pwm.ChangeDutyCycle(10) # right +90 deg position
        sleep(.25)

        pwm.stop()

        return

def quotes():
        GPIO.output(26, False) # turns off button led
        os.system(random.choice(List)) # play sound file
        return

p1 = multiprocessing.Process(target=servo_control())
p2 = multiprocessing.Process(target=quotes())


while True:
        GPIO.output(26, True) # turn on button led
        input_state = GPIO.input(18) # primes the button!
        if input_state == False:
                p1.start()
                p2.start()

                p1.join()
                p2.join()

                # servo_control()
                # quotes()



        GPIO.output(26, True) # turns button led back on
        time.sleep(0.2)
