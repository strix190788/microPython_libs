from AnalogSensor import AnalogSensor

left_sensor = AnalogSensor(26)

from time import sleep

while 1:
    sleep(0.5)
    print(left_sensor.read())