from neopixel import Neopixel
pixels = Neopixel(36, 0, 8)

import time
pixels.brightness(100)
pixels.set_pixel_line_gradient(0, 11, [255,0,0], [0,255,0])
pixels.set_pixel_line_gradient(12, 23, [0,0,255], [0,255,0])
pixels.set_pixel_line_gradient(24, 35, [255,0,0], [0,0,255])
pixels.show()
time.sleep(15)
for i in range(36):
    pixels.set_pixel(i, [0,0,0])
pixels.show()

