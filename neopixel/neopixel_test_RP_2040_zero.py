from neopixel import Neopixel
pixels = Neopixel(1, 0, 16)

import time

pixels.set_pixel(0, [255,0,0])
pixels.show()
time.sleep(2)
pixels.set_pixel(0, [0,255,0])
pixels.show()
time.sleep(2)
pixels.set_pixel(0, [0,0,255])
pixels.show()
time.sleep(5)
pixels.set_pixel(0, [0,0,0])
pixels.show()
