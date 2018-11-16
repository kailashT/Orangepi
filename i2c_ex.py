#!/usr/bin/python
#http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2



import smbus
import time

bus = smbus.SMBus(0)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
print(bus)
DEVICE_ADDRESS = 0x37      #7 bit address (will be left shifted to add the read write bit)
DEVICE_REG = 0xaa
DEVICE_REG_LEDOUT0 = 0x1d

val = 0
while(1):
	val2 = val
	val = bus.read_word_data(DEVICE_ADDRESS,DEVICE_REG)
	if(val2 != val):
		print(val)
	
