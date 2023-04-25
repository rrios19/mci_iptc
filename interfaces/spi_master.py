import threading 
import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(11,gpio.OUT)  #SCLK
gpio.setup(8, gpio.OUT)  #SS
gpio.setup(10,gpio.OUT)  #MOSI
gpio.setup(9, gpio.IN)   #MISO

gpio.output(8,gpio.HIGH)

CLK_STATE = False

def spi_sclk(Fs):
    Ts = 1/Fs
    while True:
        gpio.output(11,gpio.HIGH)
        CLK_STATE = True
        sleep(Ts)
        gpio.output(11,gpio.LOW)
        CLK_STATE = False
        sleep(Ts)

def spi_mosi(cmd):
    size = len(cmd)
    print(size)
    gpio.output(8,gpio.LOW)
    sleep(5)
    # send here
    gpio.output(8,gpio.HIGH)
    


Fs = 400
sclk_thread = threading.Thread(target=spi_sclk,args=(Fs,))
sclk_thread.start()

spi_mosi('hola')

#while True:
#    input("Hola")
#    gpio.output(8,gpio.LOW)
#    input("Hola")
#    gpio.output(8,gpio.HIGH)

    


gpio.cleanup()
