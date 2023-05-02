import sys
import threading
import RPi.GPIO as gpio
from time import sleep

#------RPI 4 Pins------
#SCLK = 11
#CS0  = 8
#CS1  = 7
#CS2  = 6
#MOSI = 10
#MISO = 9
#----------------------

class iface_handler:

    def __init__(self,fs,SCLK,CS0,CS1,CS2,MOSI,MISO):
        # ------------ Pin ------------
        self.SCLK = SCLK
        self.CS   = CS0 # Default
        self.MOSI = MOSI
        self.MISO = MISO
        # ----------- Setup -----------
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        gpio.setup(SCLK,gpio.OUT) #SCLK
        gpio.setup(CS0, gpio.OUT) #CS0
        gpio.setup(CS1, gpio.OUT) #CS1
        gpio.setup(CS2, gpio.OUT) #CS2
        gpio.setup(MOSI,gpio.OUT) #MOSI
        gpio.setup(MISO,gpio.IN ) #MISO
        # ------ Initialize pins ------
        gpio.output(CS0,gpio.HIGH)
        gpio.output(CS1,gpio.HIGH)
        gpio.output(CS2,gpio.HIGH)
        gpio.output(MOSI,gpio.LOW)
        # --------- Variables ---------
        self.data_out = []
        self.data_in =  []
        self.clk_enable  = True
        self.read_enable = False
        self.response    = None
        self.ts = 1/fs

    # Thread for slave clock
    def spi_clk(self):
        while self.clk_enable:
            gpio.output(self.SCLK,gpio.HIGH)
            if (self.read_enable):
                self.master_in()
            sleep(self.ts)
            gpio.output(self.SCLK,gpio.LOW)
            try:
                self.master_out()
                gpio.output(self.CS,gpio.LOW)
                self.read_enable = True
            except:
                gpio.output(self.CS,gpio.HIGH)
                gpio.output(self.MOSI,gpio.LOW)
                self.read_enable = False
                self.fetch_data()
            sleep(self.ts)
        gpio.cleanup()

    # Read in Master In, Slave Out
    def master_in(self):
        if (gpio.input(self.MISO)):
            self.data_in.append(1)
        else:
            self.data_in.append(0)

    # Write in Master Out, Slave In
    def master_out(self):
        gpio.output(self.MOSI,self.data_out.pop(0))

    def fetch_data(self):
        bit_count = 0
        data = 0
        if (len(self.data_in) == 32):
            while (bit_count < 32):
                bit_state = self.data_in.pop(0)
                data <<= 1
                data |= bit_state
                bit_count += 1
            self.response = data

    # Set the queue and send the data by MOSI
    def send_data(self,data_to_send):
        bit_count = 0
        queue_to_send = []
        while (bit_count < 32):
            queue_to_send.insert(0, data_to_send & 1)
            data_to_send >>= 1
            bit_count += 1
        # Send the data:
        self.data_out = queue_to_send

    # Create  and start the clock thread
    def start_clk(self):
        sclk_thread = threading.Thread(target=self.spi_clk)
        sclk_thread.start()
    
    def get_data(self):
        data = self.response
        self.response = None
        return data
    
    def change_device(self,device):
        self.CS = device

    #def check_device(self):
        #self.

    def kill_spi(self):
        self.clk_enable = False


