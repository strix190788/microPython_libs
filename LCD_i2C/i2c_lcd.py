
import time

class I2cLcd:
    def __init__(self, i2c, addr, rows, cols):
        self.i2c = i2c
        self.addr = addr
        self.rows = rows
        self.cols = cols
        self.backlight = 0x08
        self._init_lcd()

    def _write(self, data):
        self.i2c.writeto(self.addr, bytes([data | self.backlight]))

    def _pulse(self, data):
        self._write(data | 0x04)
        time.sleep_us(1)
        self._write(data & ~0x04)
        time.sleep_us(50)

    def _send(self, value, mode=0):
        high = value & 0xF0
        low = (value << 4) & 0xF0
        self._pulse(high | mode)
        self._pulse(low | mode)

    def _init_lcd(self):
        time.sleep_ms(50)
        self._pulse(0x30)
        time.sleep_ms(5)
        self._pulse(0x30)
        time.sleep_us(150)
        self._pulse(0x30)
        self._pulse(0x20)
        self._send(0x28)
        self._send(0x0C)
        self._send(0x06)
        self.clear()

    def clear(self):
        self._send(0x01)
        time.sleep_ms(2)

    def move_to(self, col, row):
        offsets = [0x00, 0x40]
        self._send(0x80 | (offsets[row] + col))

    def putstr(self, text):
        for char in text:
            self._send(ord(char), 1)
