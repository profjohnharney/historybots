# Setting up the hardware  

At this point, you should have a Raspberry Pi that can boot up into the Raspbian OS. 
You can find information on how to do this [here](https://github.com/profjohnharney/historybots/blob/working_towards_1.0/docs/set_up_rpi.md).

## RPi Hardware Basics

The beauty of the Raspberry Pi lies in its GPIO pins. 
These pins allow you to use the Pi as an interface between software and hardware. 
There is huge potential here, but for our purposes the pins will do three simple things:
- light up an LED that signals the History Bot is "working"
- confirm whether a button has been pressed or not
- light up another LED inside the button

You do not want to just throw the Pi around or to be too careless with its GPIO pins; but it is fairly robust. 
Do not be too scared.
Just remember that each connection needs two pins: one that is providing current and one that is grounded.

You can find a fantastic diagram/explainer on the Raspberry Pi pinout layout [here](https://pinout.xyz/). Note that there are two separate ways to identify pins on the Raspberry Pi: BCM and board. The [historybot.py](../historybot.py) file in this project uses BCM.

You should make sure your Raspberry Pi is unplugged when setting up connections to GPIO pins. Also be sure to double check you have connected a ground pin. Better safe than sorry.

## Hooking up audio

This *should* be easy. Just plug in your speaker and go! The Raspberry Pi works with analog input in a very straightforward way. USB might be trickier; if you are not hearing anything check the solution in the RPi [setup](/set_up_rpi.md).

## Hooking up your indicator LED

Your LED has two legs, one of which is longer: this longer leg is positive (anode) and the shorter leg is negative (cathode).

If you have bought the supplies recommended by this guide, you should use a resistor when connecting the LED to your board. The female/female jumper wires are an excellent tool for this job, especially if you are starting. 

Here is a nice, clear explainer on connecting LEDs [from Adafruit](https://makecode.adafruit.com/learnsystem/pins-tutorial/devices/led-connections).

## Hooking up the button

The button is the trickiest part of the project to pull off, especially if (like me, when I started this) you have no soldering experience. You can certainly prototype with alligator clips, but be aware you will be placing the jaws of the clips in tight proximity to each other. Do not let the metal parts of these cables touch.

The button recommended in this guide has a resistor built in, which is nice! You are effectively making two sets of connections: one is for the LED (which is similar to the step above) and the other is for the button.