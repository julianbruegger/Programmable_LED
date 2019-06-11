import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 30)

pixels[0] = (255, 0, 0)
pixels[2] = (0, 255, 0)
pixels[5] = (0, 0, 255)
