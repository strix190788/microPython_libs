from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
import framebuf,sys

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                            # oled display height

image_byte_arr = b'BM\xbe\x00\x00\x00\x00\x00\x00\x00>\x00\x00\x00(\x00\x00\x00 \x00\x00\x00 \x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x80\x00\x00\x00\xc4\x0e\x00\x00\xc4\x0e\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xfc?\xff\xff\xfb\xcf\xff\xff\xe7\xf7\xff\xff\xc7\xf1\xff\xffs\xc6\x7f\xfe\xf1\xcf\xbf\xfd\xf7\xef\xbf\xfd\xf7\xf7\xdf\xff\xff\xf7\xdf\xfb\xef\xf3\xdf\xf9\xc7\xf1\x8f\xf6\x13\xeco\xf7|>w\xf7~\x7fw\xf7\xfe\x7fw\xf7\xff\x7fo\xfb\x7f\x7fo\xfc~~\x1f\xfd\xbc=\xff\xff\xe3\xe3\xbf\xfe\xf7\xf7\xbf\xff\x7f\xff\x7f\xff3\xe4\xff\xffx\x1f\x7f\xfe\xfc?\xbf\xfd\xfe?\xff\xfb\xff\x7f\xdf\xfb\xff\x7f\xdf\xfb\xfe\x7f\xef\xfb\xff\xbf\xef\xf9\xfb\xdf\x9f\xff\x0f\xf0\xff'
image_width = 32
image_height = 32

#OLED I2C Configuration
i2c = I2C(0, scl=Pin(5), sda=Pin(4)) #Init I2C using pinsGP17&GP16 (defaultI2C0 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
utime.sleep(1)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c) # Init oled display



#OLED Text display Function
def displayText(text, position=(0,0),clear_oled=True,show_text=True):
    if clear_oled:
        oled.fill(0) # Clear the oled display in case it has junk on it.
    oled.text(text,position[0],position[1]) # dispaying text
    if show_text:
        oled.show()  # Updating the display
        
        
#OLED Image display function
        
def displayImage(image_byte_array, image_resolution,position=(0,0),clear_oled=False,show_img=True):
    img = bytearray(image_byte_array)
    img = bytearray([img[i] for i in range(len(img)-1,-1,-1)])
    
    frame = framebuf.FrameBuffer(img, image_resolution[0], image_resolution[1], framebuf.MONO_HMSB) # MONO_HLSB, MONO_VLSB, MONO_HMSB
    
    if clear_oled:
        oled.fill(0) # clear the OLED
        print("clear")
    if show_img:
        oled.blit(frame, position[0],position[1]) # show the image at location (x=0,y=0)
        oled.show()
        
        print("display")


def display_sign(x,y):
    oled.hline(x+5,y,5,1)
    oled.hline(x+3,y+1,2,1)
    oled.hline(x+10,y+1,2,1)
    oled.hline(x+2,y+2,1,1)
    oled.hline(x+11,y+2,2,1)
    oled.vline(x+1,y+3,2,1)
    oled.hline(x+5,y+3,2,1)
    oled.hline(x+5,y+4,2,1)
    oled.hline(x+11,y+3,2,1)
    oled.hline(x+11,y+4,2,1)
    oled.vline(x,y+5,5,1)
    oled.vline(x+1,y+10,2,1)
    oled.vline(x+2,y+11,2,1)
    oled.hline(x+11,y+4,3,1)
    oled.hline(x+11,y+5,4,1)
    oled.hline(x+10,y+6,5,1)
    oled.hline(x+9,y+7,6,1)
    oled.hline(x+7,y+8,8,1)
    oled.hline(x+6,y+9,2,1)
    oled.hline(x+10,y+9,5,1)
    oled.hline(x+5,y+10,3,1)
    oled.hline(x+10,y+10,4,1)
    oled.hline(x+5,y+11,9,1)
    oled.hline(x+6,y+12,7,1)
    oled.hline(x+3,y+13,2,1)
    oled.hline(x+7,y+13,5,1)
    oled.hline(x+5,y+14,5,1)
    

def flag():
    oled.hline(1,0,5,1)
    oled.vline(1,0,20,1)
    oled.hline(0,1,9,1)
    oled.hline(5,2,21,1)
    oled.hline(16,1,9,1)
    
    
#--------------BEGIN---------------

#oled.fill(0)
#oled.rect(30,40,5,5, 1) # x,y,w,h,color
#oled.ellipse(40, 50, 5, 2, 1) # ellipse(x, y, xr, yr, c)
#oled.rect(100, 10, 5, 5, 1)
#oled.text("Thanks, dad!", 10, 0)
#oled.pixel(64, 32, 1) # x, y, цвет
#display_sign(32,16)
#oled.line(64,0,123,63, 1)
#oled.hline(32, 20, 20, 0) # x,y, длина, цвет
##oled.hline(32, 20, 20, 0) # x,y, длина, цвет
#oled.show()
#displayImage(image_byte_arr,(image_width,image_height),(64,32),clear_oled=False)
#oled.invert(1)# инверсия

#flag()
#oled.ellipse(50, 30, 30, 30, 1)
#oled.hline(40,40,20,1)
#oled.ellipse(60, 50,30,30,1)

oled.show()
        



    