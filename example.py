# ADXL345 Python example 
#
# author:  Jonathan Williamson
# license: BSD, see LICENSE.txt included in this package
# 
# This is an example to show you how to use our ADXL345 Python library
# http://shop.pimoroni.com/products/adafruit-triple-axis-accelerometer

from adxl345 import ADXL345
import time
adxl345 = ADXL345()
print("ADXL345 on address 0x%x:" % (adxl345.address))
while True:
    axes = adxl345.getAxes(True)
    print(axes['x'])
    time.sleep(0.1)    
