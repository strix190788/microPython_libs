from utime import sleep
from hcsr04 import HCSR04
sonic = HCSR04(14,15)
while 1:
    print(sonic.distance_cm())
    sleep(1)
    
    