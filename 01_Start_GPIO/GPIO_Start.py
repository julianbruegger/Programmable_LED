import RPi.GPIO as GPIO
import os

# Define a callback function that will be called by the GPIO
# event system:
def onButton(channel):
    if channel == 16:
        os.system("/home/pi/rpi_ws281x/python/examples/Rainbow.py")

# Setup GPIO16 as input with internal pull-up resistor to hold it HIGH
# until it is pulled down to GND by the connected button: 
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Register an edge detection event on FALLING edge. When this event
# fires, the callback onButton() will be executed. Because of
# bouncetime=20 all edges 20 ms after a first falling edge will be ignored: 
GPIO.add_event_detect(16, GPIO.FALLING, callback=onButton, bouncetime=20)

# The script would exit now but we want to wait for the event to occure
# so we block execution by waiting for keyboard input so every key will exit
# this script
input()