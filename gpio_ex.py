import OPi.GPIO as GPIO
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import json
import time
import signal
import sys
import logging

GPIO.setmode(GPIO.BOARD)
'''

BOARD = {
    3: 12,    # I2C0_SDA/PA12 (TWI0_SDA/DI_RX/PA_EINT12)
    5: 11,    # I2C0_SCL/PA11 (TWI0_SCK/DI_TX/PA_EINT11)
    7: 6,     # PA6 (SIM_PWREN/PWM1/PA_EINT6)
    8: 13,    # PA13 (SPI1_CS/UART3_TX/PA_EINT13)
    10: 14,   # PA14 (SPI1_CLK/UART3_RX/PA_EINT14)
    11: 1,    # PA1 (UART2_RX/JTAG_CK/PA_EINT1)
    12: 110,  # PD14
    15: 3,    # PA3 (UART2_CTS/JTAG_DI/PA_EINT3)
    16: 68,   # PC4
    18: 71,   # PC7
    19: 64,   # PC0 (SPI0_MOSI)
    21: 65,   # PC1 (SPI0_MISO)
    22: 2,    # PA2 (UART2_RTS/JTAG_DO/PA_EINT2)
    23: 66,   # PC2 (SPI0_CLK)
    24: 67,   # PC3 (SPI0_CS)
    26: 21,   # PA21 (PCM0_DIN/SIM_VPPPP/PA_EINT21)
    27: 19,   # PA19 (PCM0_CLK/TWI1_SDA/PA_EINT19)
    28: 18,   # PA18 (PCM0_SYNC/TWI1_SCK/PA_EINT18)
    29: 7,    # PA7 (SIM_CLK/PA_EINT7)
    31: 8,    # PA8 (SIM_DATA/PA_EINT8)
    32: 200,  # PG8 (UART1_RTS/PG_EINT8)
    33: 9,    # PA9 (SIM_RST/PA_EINT9)
    35: 10,   # PA10 (SIM_DET/PA_EINT10)
    36: 201,  # PG9 (UART1_CTS/PG_EINT9)
    37: 20,   # PA20 (PCM0_DOUT/SIM_VPPEN/PA_EINT20)
    38: 198,  # PG6 (UART1_TX/PG_EINT6)
    40: 199,  # PG7 (UART1_RX/PG_EINT7)
		
		3: 12,
        5: 11,
        7: 6,
        8: 198,
        10: 199,
        11: 1,
        12: 7,
        13: 0,
        15: 3,
        16: 19,
        18: 18,
        22: 2,
        24: 13,
        26: 10
		23: 14,
		19: 15,
        21: 16,
}

'''

logging.basicConfig(filename='GPIOlog.txt',
    filemode='a',
    format='%(asctime)-8s | %(levelname)-6s | %(lineno)4s |%(funcName)15s() | %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG,
)


def handler(signum, frame):
    GPIO.cleanup()
    time.sleep(1)
    sys.exit()


def doorremove():
    pass


def door1(pin):
	print ("pin 3 is toggle")
	time.sleep(1)

def door2(pin1):
	print ("pin 5 is toggle")
	time.sleep(1)

def door3(pin2):
	print ("pin 8 is toggle")
	time.sleep(1)	

def door4(pin3):
	print ("pin 11 is toggle")
	time.sleep(1)		

if __name__ == '__main__':
	logging.debug("init signal ")
	signal.signal(signal.SIGINT, handler)
	
	
	logging.debug("configuring gpio")
	# gpio configuration
	
	
	pin = 3
	GPIO.setup(pin, GPIO.IN)
	GPIO.add_event_detect(pin, GPIO.BOTH, callback=door1)
	
	pin1 = 5
	GPIO.setup(pin1, GPIO.IN)
	GPIO.add_event_detect(pin1, GPIO.BOTH, callback=door2)
	
	pin2 = 7
	GPIO.setup(pin2, GPIO.IN)
	GPIO.add_event_detect(pin2, GPIO.BOTH, callback=door3)

	pin4 = 23
	GPIO.setup(pin4, GPIO.OUT)
	
	pin5 = 19
	GPIO.setup(pin5, GPIO.OUT)
	
	pin6 = 21
	GPIO.setup(pin6, GPIO.OUT)
	

	
	while True:
		print("HIGH")
		GPIO.output(pin4, GPIO.HIGH)
		GPIO.output(pin5, GPIO.HIGH)
		GPIO.output(pin6, GPIO.HIGH)
		time.sleep(1)
		print("LOW")
		GPIO.output(pin4, GPIO.LOW)
		GPIO.output(pin5, GPIO.LOW)
		GPIO.output(pin6, GPIO.LOW)
		time.sleep(1)

'''
23: 14,
		19: 15,
        21: 16,
'''	
