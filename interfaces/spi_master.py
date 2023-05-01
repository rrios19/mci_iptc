import sys
import threading
import RPi.GPIO as gpio
from time import sleep

#------RPI 4 Pins------
SCLK = 11
CS0  = 8
CS1  = 7
CS2  = 6
MOSI = 10
MISO = 9
#----------------------


# Set SPI interface
def set_spi():
    gpio.setmode(gpio.BCM)
    gpio.setup(SCLK,gpio.OUT) #SCLK
    gpio.setup(CS0,  gpio.OUT) #CS0
    gpio.setup(CS1,  gpio.OUT) #CS1
    gpio.setup(CS2,  gpio.OUT) #CS2
    gpio.setup(MOSI,gpio.OUT) #MOSI
    gpio.setup(MISO,gpio.IN ) #MISO
    # ------ Initialize pins ------
    gpio.output(CS0,gpio.HIGH)
    gpio.output(CS1,gpio.HIGH)
    gpio.output(CS2,gpio.HIGH)
    gpio.output(MOSI,gpio.LOW)

# Thread for slave clock
def spi_sclk(Fs):
    global data_out
    global data_in
    global running
    running = True
    Ts = 1/Fs # BUG
    read_enable = False
    while running:
        gpio.output(SCLK,gpio.HIGH)
        if (read_enable):
            master_in(data_in)
        sleep(Ts)
        gpio.output(SCLK,gpio.LOW)
        try:
            master_out(data_out.pop(0))
            gpio.output(CS0,gpio.LOW)
            read_enable = True
        except:
            gpio.output(CS0,gpio.HIGH)
            gpio.output(MOSI,gpio.LOW)
            read_enable = False
        sleep(Ts)
    gpio.cleanup()

# Write in Master Out, Slave In
def master_out(bit_state):
    gpio.output(MOSI,bit_state)

# Read in Master In, Slave Out
def master_in(data):
    if (gpio.input(MISO)):
        data.append(1)
    else:
        data.append(0)

def set_queue(data):
    count = 0
    queue = []
    while (count < 32):
        queue.insert(0, data & 1)
        data >>= 1
        count += 1
    return queue

def start_sclk(Fs):
    global data_in
    data_in = []
    set_spi()
    sclk_thread = threading.Thread(target=spi_sclk,args=(Fs,))
    sclk_thread.start()

def change_device():


def main_spi(data,run):
    global data_out
    global data_in
    global running
    data_out = set_queue(data)
    running = run

#main_spi(1,0xFA43F54A)
