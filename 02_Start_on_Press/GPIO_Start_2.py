# Dieses Script soll ein LED-Lauflicht starten sobald GPIO18 mit Ground verbunden ist.
# Wenn keine Verbindung zusande kommt, sollen die ersten und die Letzten LED's Leuchten.
# ICT-Berufsbildung Zentralschweiz
# Julian Bruegger (julian.bruegger@ict-bz.ch)
# 24.06.2019

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import RPi.GPIO as GPIO
import os
import sys
from subprocess import Popen
import argparse


# LED pixels configuration:
num_pixels     = 60      # Number of LED pixels.
pixel_pin      = board.D12      # GPIO pin connected to the pixels (18 uses PWM!).
ORDER          = neopixel.GRB


# Config_GPIO_Play
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set states for GPIO_Play
last_state1 = True
input_state1 = True
player = True


pixels = neopixel.NeoPixel(pixel_pin, num_pixels)
    

#Read states of inputs
input_state1 = GPIO.input(18)

#If GPIO(18) is shorted to Ground


if input_state1 != last_state1:
    if (player and not input_state1):
        pixels.fill((229, 0, 124))
        time.sleep(4)
        pixels[0] = (0, 255,0)
        pixels[1] = (0, 254, 1)
        pixels[2] = (0, 253, 2)
        pixels[3] = (0, 252, 3)
        pixels[4] = (0, 251, 4)
        pixels[5] = (0, 255, 0)
        pixels[6] = (0, 255, 0)
        pixels[7] = (0, 255, 0)
        pixels[8] = (0, 255, 0)
        pixels[9] = (0, 255,0)
        pixels[10] = (0, 254, 1)
        pixels[11] = (0, 253, 2)
        pixels[12] = (0, 252, 3)
        pixels[13] = (0, 251, 4)
        pixels[14] = (0, 255, 0)
        pixels[15] = (0, 255, 0)
        pixels[16] = (0, 255, 0)
        pixels[17] = (0, 255, 0)

        time.sleep(10)
        pixels.fill((0, 0, 0))
        player = True
        

    elif not input_state1:
        pixels.fill((229, 0, 124))
        time.sleep(7)
        pixels.fill((0, 157, 122))
        time.sleep(5)
        pixels.fill((0, 0, 0))
        player = True
        
            
#If omxplayer is running and GIOP(17) is not shorted to Ground
elif (player and input_state1):
    pixels[0] = (255, 0, 0)
    pixels[143] = (255, 0, 0)
    player = False
    time.sleep(5)
    pixels.fill((0, 0, 0))

#Set last_input states
last_state1 = input_state1