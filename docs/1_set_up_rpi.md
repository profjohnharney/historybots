# How to set up your Raspberry Pi

## Get a Raspberry Pi!

I have used both a Raspberry Pi 3B+ and a Raspberry Pi Zero W. Amazon sells decent bundles including a case and power supply. 
I recommend shopping at either [Sparkfun](https://www.sparkfun.com/) or [Adafruit](https://www.adafruit.com/). I have had excellent experiences with both.

## Get your Pi working as a computer!

There are three main tasks here:
- download an operating system; I recommend [Raspbian Pi OS](https://www.raspberrypi.org/downloads/raspberry-pi-os/).
- flash the operating system to your SD card; I recommend using [Raspberry Pi Imager](https://www.raspberrypi.org/downloads/).
- hook your RPi up to a monitor and keyboard, and plug it in! (I would also go ahead and plug in the USB speaker).

## Initial setup

Default username for every RPi is "pi", and the default password is "raspberry".

Beyond that, everything should be fairly straightforward. There is a good setup guide [here](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up).

## Using the Raspberry Pi (and the command line)

Once you are all set up and logged in, you will be able to use the desktop environment. 
Getting to know this environment is a good idea, and it is a straightforward transition from using a Windows PC or a Mac.

At some point you will want to start getting to know the command line.
You can open a terminal in Raspberry Pi OS by pressing `Ctrl+Alt+T`.
If you run into issues and find yourself googling, you will be doing a lot of typing things into the command line.
However, if all goes well your use of the command line will be limited to typing `python historybot.py`.

My main advice to you, as someone whose main experience with the command line before starting this project was limited to using DOS in the 1980s, is to take simple steps. 
Use the command line as needed and go from there. 
There is a lot of depth to the command line, but this project only requires some fairly light usage of it.
So do not be intimidated.

## USB audio fix (if needed)

You may have issues getting your RPi to play audio through the USB speaker. 
If this is the case, I strongly recommend the advice [here](https://www.raspberrypi-spy.co.uk/2019/06/using-a-usb-audio-device-with-the-raspberry-pi/), particularly under "Set USB Audio as Default Audio Device." 

## Some extra steps

### Install espeak

You need [espeak](http://espeak.sourceforge.net/) for any History Bot using text files rather than audio files.

1. Open your terminal on your Raspberry Pi either by selecting it from the menu or pressing `CTRL+ALT+T`.
2. Type ```sudo apt-get install espeak```; you may be asked to press Y to confirm installation
3. Now that espeak is installed, it should theoretically work with the syntax ```espeak "hello world"```; this might not be the case on your RPi. 
Do not fret, you just need to use a different command: ```espeak --stdout "hello world" | aplay```. This should work just fine.

### SSH (Secure Shell)

Once you've got your feet wet with the RPi, I recommend setting it up so you can access it via wifi without having to connect it to a monitor and keyboard every time. 
You can find more information [here](https://www.raspberrypi.org/documentation/remote-access/ssh/). For now though, it's not vital.
