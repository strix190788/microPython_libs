from time import sleep
from servo import Servo
s = Servo(16)
while 1:
    for i in range(180):
        s.write(i)
        sleep(0.1)
    for i in range(180,0,-1):
        s.write(i)
        sleep(0.1)