#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Julian Bruegger (julian.bruegger@ict-bz.ch)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_Neopixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_CHANNEL)
strip.brgin()

for x in range (0, LED_COUNT):
        strip.setPixelColor(x, Color(0,255,255))
strip.show