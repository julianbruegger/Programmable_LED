#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(20)
    if input_state == False:
        print('Button Pressed')
        os.system('sudo python3 /home/pi/GPIO_Start.py & sudo python3 /home/pi/GPIO_Start_2.py')
        time.sleep(0.2)