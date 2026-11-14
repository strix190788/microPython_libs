from machine import Pin, ADC, PWM
from utime import sleep
import utime
class MotorTrain_L9110:
    def __init__(self, left_dir, left_speed, right_dir, right_speed):
        self.__left_dir = Pin(left_dir, Pin.OUT)
        self.__left_speed = PWM(Pin(left_speed))
        self.__right_dir = Pin(right_dir, Pin.OUT)
        self.__right_speed = PWM(Pin(right_speed))
        
        self.__left_dir.off()
        self.__right_dir.off()
        
        self.__left_speed.freq(1000)
        self.__right_speed.freq(1000)
        self.__max_power = 655
        
        self.left_revers = False
        self.right_revers = False
    
    
    def reverse_right_motor(self):
        self.right_revers = True
        
    def reverse_left_motor(self):
        self.left_revers = True
        
    def stop(self):
        self.__left_speed.duty_u16(0)
        self.__right_speed.duty_u16(0)
        sleep(0.1)
    
    def set_max_power(self, pwr):
        pwr = int(pwr)
        if pwr > 0 and pwr <= 655 : self.__max_power = pwr
    
    # мощность задаётся в процентах
    def move(self, left_pwr, right_pwr, *args): 
        if len(args) > 0:
            self.move(left_pwr, right_pwr)
            sleep(args[0])
            self.stop()
        else:
            left_pwr = int(left_pwr)
            right_pwr = int(right_pwr)
            if left_pwr < -100: left_pwr = -100
            if right_pwr < -100: right_pwr = -100
            if left_pwr > 100: left_pwr = 100
            if right_pwr > 100: right_pwr = 100
            
            if left_pwr >= 0:
                if self.left_revers:
                    self.__left_dir.off()
                else:
                    self.__left_dir.on()
            else:
                if self.left_revers:
                    self.__left_dir.on()
                else:
                    self.__left_dir.off()
                
            if right_pwr >= 0:
                if self.right_revers:
                    self.__right_dir.off()
                else:
                    self.__right_dir.on()
            else:
                if self.right_revers:
                    self.__right_dir.on()
                else:
                    self.__right_dir.off()
                
            left_pwr = abs(left_pwr)
            right_pwr = abs(right_pwr)
            self.__left_speed.duty_u16(left_pwr * self.__max_power)
            self.__right_speed.duty_u16(right_pwr * self.__max_power)
                
                
    def p_move(self, error, pwr, kp, *args):
        if len(args) > 0:
            curr_time = utime.time()
            while utime.time() - curr_time < args[0]:
                self.p_move(error, pwr, kp)
            self.stop()
        else: self.move(pwr - error * kp, pwr + error * kp)
    
