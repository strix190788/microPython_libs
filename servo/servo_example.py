from machine import Pin, PWM
from servo import Servo
s = Servo(16)
s.write(180)