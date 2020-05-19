# John Harney, Centre College, updated 05.20.20

# this is the "Caesar bot", a history bot based on Julius Caesar
# this is an example of how to write a bot using text-to-speech but without Raspberry Pi hardware

# this code is based on the idea you will place (theoretically short)
# plain text files in the same directory as the script

import os # for commands via console
import random

# maybe change the next few lines to a function, not sure

l_dirlist = os.listdir()
l_textfiles = []

# code takes text files in the SAME directory as the script
# espeak must be installed on your computer for this to work
# for details consult the site or go to: http://espeak.sourceforge.net/

for file in l_dirlist:
    if file[-4:] == ".txt":
        l_textfiles.append("espeak -f " + file) # espeak requires the -f option; otherwise it reads out the filename

i_count = 0 # this counter is used so notification uses correct grammar
answer_list = ["yes", "sure", "okay", "ok", "y", "why not", "why not?"] # list is used to avoid a long sequence of possible answers below

# following code is where the magic happens
while True:
    answer = input("Welcome to the Caesar bot! Would you like to hear from Caesar? ") # I could not resist making the text specific; to use this code for another no-hardware bot, you will have to edit text.
    lower_answer = answer.lower() # converts the user's answer to lowercase
    if lower_answer in answer_list:
        i_count = i_count + 1
        os.system(random.choice(l_textfiles)) # takes random file from list and plays through command line
        if i_count == 1:
            print("Caesar Bot has been activated!")
        else:
            print("Caesar Bot has been activated " + str(i_count) + " times!")
    else:
        print("Oh... okay. See you next time!")
        break # this gets the user out of the loop; note that Ctrl+C will typically cancel a python script
        