from machine import Pin, ADC
class AnalogSensor():
    def __init__(self, pin):
        self.sensor = ADC(Pin(pin))
        
    def read(self):
        return self.sensor.read_u16() // 655