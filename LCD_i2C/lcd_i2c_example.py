from machine import Pin, I2C
from time import sleep
from i2c_lcd import I2cLcd
sleep(0.1)

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)


lcd.clear()
lcd.putstr("SYSTEM NORMAL")
lcd.move_to(0, 1) # 0 - верхняя строка, 1 - левый символ
lcd.putstr("any text ")