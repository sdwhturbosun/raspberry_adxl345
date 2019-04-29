import wiringpi as wpi
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
devaddr=0x53#sdo_altaddress---->gnd:0x53;sdo_altaddress--->3.3v:0x1D
int1=21
int2=20
led_inact=13
led_act=6
gpio.setwarnings(False)
gpio.setup(int2,gpio.OUT)
gpio.output(int2,0)
gpio.setup(int1,gpio.OUT)
gpio.output(int1,0)
gpio.setup(int1,gpio.IN)
gpio.setup(int2,gpio.IN)
gpio.setup(led_inact,gpio.OUT)
gpio.setup(led_act,gpio.OUT)

def getint(pin):
    print("int detected,port:"+str(pin))


device=wpi.wiringPiI2CSetup(devaddr)
wpi.wiringPiI2CWriteReg8(device,0x2D,0x20)
deviceid=wpi.wiringPiI2CReadReg8(device,0x00)
print("device id:"+str(deviceid))
wpi.wiringPiI2CWriteReg8(device,0x2E,0x00)#disable int
wpi.wiringPiI2CWriteReg8(device,0x24,0x08)#dongtai fazhi
wpi.wiringPiI2CWriteReg8(device,0x25,0x04)#jingzhi fazhi
wpi.wiringPiI2CWriteReg8(device,0x26,0x04)#jingzhi shijian
wpi.wiringPiI2CWriteReg8(device,0x27,0xff)#act inact kongzhi

wpi.wiringPiI2CWriteReg8(device,0x2F,0x10)#int map
wpi.wiringPiI2CWriteReg8(device,0x31,0x0B)#data format
wpi.wiringPiI2CWriteReg8(device,0x2C,0x0a)#data rate
wpi.wiringPiI2CWriteReg8(device,0x2E,0x18)#enable int
wpi.wiringPiI2CWriteReg8(device,0x2D,0x38)#power ctrl,lianjie moshi
#gpio.add_event_detect(int1,gpio.FALLING,callback=getint)
gpio.add_event_detect(int2,gpio.RISING,callback=getint)
gpio.add_event_detect(int1,gpio.RISING,callback=getint)
while True:
    
   
    time.sleep(0.01)
    c=wpi.wiringPiI2CReadReg8(device,0x30)
    if (c&0x10):
        print(time.strftime("%H:%M:%S",time.localtime())+" actived!interrupt value:"+str(c))
    if (c&0x08):
        print(time.strftime("%H:%M:%S",time.localtime())+" inactived!interrupt value:"+str(c))

