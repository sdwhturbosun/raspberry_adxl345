import wiringpi as wpi
import time
import RPi.GPIO as gpio
devaddress=0x53
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
int1=21
int2=20
gpio.setup(int2,gpio.IN)
def int2interrupt(pin):
    
    c=wpi.wiringPiI2CReadReg8(device,0x30)
    if(c&0x20):
        print(time.strftime("%H:%M:%S",time.localtime())+" double tap detected!")
gpio.add_event_detect(int2,gpio.RISING,callback=int2interrupt)
device=wpi.wiringPiI2CSetup(devaddress)

#detect double tap
wpi.wiringPiI2CWriteReg8(device,0x2D,0x00)#pw ctl autosleep=1   
wpi.wiringPiI2CWriteReg8(device,0x2E,0x00)#int enable disable int:  先关闭中断，再设置中断，然后再开启
wpi.wiringPiI2CWriteReg8(device,0x2E,0x20)#int enable  double=1
wpi.wiringPiI2CWriteReg8(device,0x2F,0x20)#int map double-->int2
wpi.wiringPiI2CWriteReg8(device,0x1D,0x3F)#thresh_tap=937.5mg
wpi.wiringPiI2CWriteReg8(device,0x21,0x10)#dur=128*625us
wpi.wiringPiI2CWriteReg8(device,0x22,0x80)#later=16*1.25ms  多久之后可以下一次点击
wpi.wiringPiI2CWriteReg8(device,0x23,0xff)#window=256*1.25ms   允许下一次点击开始，留给下一次点击的时间窗口，在这个窗口内点击算双击，离开这个窗口算下一次单击
wpi.wiringPiI2CWriteReg8(device,0x2A,0x07)#tap ctl  ,very important  很重要，检测单击双击必须设置xyz是否允许点击。
#wpi.wiringPiI2CWriteReg8(device,0x2c,0x0a)#data rate
wpi.wiringPiI2CWriteReg8(device,0x31,0x08)#data format
wpi.wiringPiI2CWriteReg8(device,0x2D,0x18)
wpi.wiringPiI2CWriteReg8(device,0x2E,0x20)#enable int

while True:
    c=wpi.wiringPiI2CReadReg8(device,0x30)
    if (c&0x20):
        print("double tap detect")
    time.sleep(0.1)

    