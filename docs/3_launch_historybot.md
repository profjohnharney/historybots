# Launching the History Bot!

Please make sure you have read the other documentation. You should now have a Raspberry Pi that boots into the Raspberry Pi OS with a keyboard, mouse, monitor, speaker, notification LED and arcade button connected.

I strongly recommend getting in the habit of jumping right into the terminal when you are using your Raspberry Pi. You can open a terminal at any time by pressing `Ctrl+Alt+T`.

Now that you are in the terminal, it will not hurt to make sure that your system is up to date.

`sudo apt-get update`  
`sudo apt-get upgrade -y`

Lots of people on the Internet will complain at my liberal use of `sudo` here. It is short for "superuser do" and it is not something to be used recklessly. However, if you are brand new to linux you are going to get a lot of "permission denied" messages, and as you can always reflash your OS on to the SD card if things go badly wrong, I would not worry too much about it.

With the system updated, you will want to install the historybot software locally on your machine. 

`git clone https://github.com/profjohnharney/historybots`  

This will install a directory named "historybots" in your home directory. You can get there by typing the following:  

`cd historybots`  

From there you can type the `ls` command to see a list of files and directories. You activate history bots from the command line using the `python` command. If you wanted to test the Muhammad Ali history bot for example, you would type the following commands:

`cd ali_bot`  
`python ali_bot.py`

You can use `Ctrl+C` to cancel the history bot program when you are done.

If you want to go back a directory, for example from the `ali_bot` directory back to the main `historybots` directory, type:  

`cd ..`

And finally, if you are ever lost, you can type `pwd` (print working directory) to see where you are.

There are many, many resources online to help you become more comfortable with the command line. [This tutorial](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview) has a lot of information - more than you need to run a history bot - but is also clearly structured and easy to navigate.
