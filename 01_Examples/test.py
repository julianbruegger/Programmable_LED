# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

# The number of NeoPixels
num_pixels = 144
# Pin the LED_Strip is connected
pixel_pin = board.D18

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)


# Set Brightness
brightness  = 100

while True:


	# Code
	brightness  = 255

	pixels[0] = (255, 0, 0)
	time.sleep(2)
	pixels[2] = (0, 255, 0)
	time.sleep(2)
	pixels[4] = (0, 0, 255)
	time.sleep(2)
	pixels[6] = (100, 100, 100)
	time.sleep(2)
	pixels[8] = (162, 188, 9)
	time.sleep(2)
	pixels[10] = (229, 0, 124)
	time.sleep(2)
	pixels[12] = (0, 170, 227)
	time.sleep(2)
	pixels[14] = (239, 124, 0)
	time.sleep(2)
	pixels[16] = (182, 23, 22)
	time.sleep(2)
	pixels[18] = (0, 157, 122)



	time.sleep(5)

	pixels[18] = (0, 0, 0)
	time.sleep(1)
	pixels[16] = (0, 0, 0)
	time.sleep(1)
	pixels[14] = (0, 0, 0)
	time.sleep(1)
	pixels[12] = (0, 0, 0)
	time.sleep(1)
	pixels[10] = (0, 0, 0)
	time.sleep(1)
	pixels[8] = (0, 0, 0)
	time.sleep(1)
	pixels[6] = (0, 0, 0)
	time.sleep(1)
	pixels[4] = (0, 0, 0)
	time.sleep(1)
	pixels[2] = (0, 0, 0)
	time.sleep(1)
	pixels[0] = (0, 0, 0)

	time.sleep(5)

