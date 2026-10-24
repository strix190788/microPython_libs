from machine import Pin, ADC, PWM
from utime import sleep
import utime
class MotorTrain_l298N:
    def __init__(self, in1, in2, in3, in4): #реверс осуществляется изменением порядка пинов подключения
        self.__left1 = PWM(Pin(in1))
        self.__left2 = PWM(Pin(in2))
        self.__right1 = PWM(Pin(in3))
        self.__right2 = PWM(Pin(in4))
        
        self.__left1.freq(1000)
        self.__left2.freq(1000)
        self.__right1.freq(1000)
        self.__right2.freq(1000)
        
        self.__in1 = in1
        self.__in2 = in2
        self.__in3 = in3
        self.__in4 = in4
        
        self.__max_power = 655
    
    
    def stop(self):
        self.__left1.duty_u16(0)
        self.__left2.duty_u16(0)
        self.__right1.duty_u16(0)
        self.__right2.duty_u16(0)
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
                self.__left1.duty_u16(left_pwr * self.__max_power)
                self.__left2.duty_u16(0)
            else:
                self.__left1.duty_u16(0)
                self.__left2.duty_u16(left_pwr * self.__max_power)
            if right_pwr >= 0:
                self.__right1.duty_u16(right_pwr * self.__max_power)
                self.__right2.duty_u16(0)
            else:
                self.__right1.duty_u16(0)
                self.__right2.duty_u16(right_pwr * self.__max_power)
        
        
    def p_move(self, error, pwr, kp, *args):
        if len(args) > 0:
            curr_time = utime.time()
            while utime.time() - curr_time < args[0]:
                self.p_move(error, pwr, kp)
            self.stop()
        else: self.move(pwr - error * kp, pwr + error * kp)
    
    
    
    