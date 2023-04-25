import threading 
import RPi.GPIO as gpio
from time import sleep

# Set SPI interface
def set_spi():
    # RPI 4 Pins
    SCLK = 11
    CS   = 8
    MOSI = 10
    MISO = 9
    # Set pins
    gpio.setmode(gpio.BCM)
    gpio.setup(SCLK,gpio.OUT)#SCLK
    gpio.setup(CS,  gpio.OUT)#CS
    gpio.setup(MOSI,gpio.OUT)#MOSI
    gpio.setup(MISO, gpio.IN)#MISO
    # Initialize pins
    gpio.output(CS,gpio.HIGH)
    gpio.output(MOSI,gpio.LOW)

# Thread for slave clock
def spi_sclk(Fs):
    global cmd
    Ts = 1/Fs
    while True:
        gpio.output(11,gpio.HIGH)
        sleep(Ts)
        gpio.output(11,gpio.LOW)
        # Always send a command if it exists
        try:
            send_bit(cmd.pop(0))
        except:
            pass
        sleep(Ts)

# Send bit by bit
def send_bit(bit):
    gpio.output(10,bit)





# Up everything works





def spi_mosi(cmd):
    global CLK_STATE
    last = CLK_STATE
    bit = len(cmd) - 1
    gpio.output(8,gpio.LOW)
    while True:
        if CLK_STATE == True and last == False:
            gpio.output(10,cmd[bit])
            print(bit)
            bit -= 1
        if bit <= -1:
            break
        last = CLK_STATE
    gpio.output(8,gpio.HIGH)
    



set_spi()
sleep(5)


Fs = 1
sclk_thread = threading.Thread(target=spi_sclk,args=(Fs,))
sclk_thread.start()

sleep(5)
cmd = [1,0,1,0,1,0,1,0]

#cmd = [1,0,1,0,1,0,1,0]
#spi_mosi(cmd)

#while True:
#    input("Hola")
#    gpio.output(8,gpio.LOW)
#    input("Hola")
#    gpio.output(8,gpio.HIGH)

    
while True:
    continue

gpio.cleanup()
