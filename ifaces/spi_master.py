# Tecnologico de Costa Rica
# Integrated Power Test system for CubeSats (IPTC)
# Control and Interface Module
# Author: Ronald Rios
# Description: SPI master
# Usage: >>> SPI = iface_handler()

"""
This script defines a class iface_handler that represents the SPI master interface.
It initializes GPIO pins, sets up the SPI interface, and configures variables.
The class includes methods for clock management (spi_clk), data transfer (master_in, master_out, fetch_data, send_data), and thread management (start_clk, kill_spi).
The SPI clock is generated in a separate thread (spi_clk), ensuring continuous clock pulses.
Data is sent and received through MOSI and MISO lines.
The script uses the RPi.GPIO library to interact with Raspberry Pi GPIO pins.
This script essentially handles SPI communication with other devices, providing methods to send and receive data. The start_clk method initiates the clock thread, and kill_spi stops the clock thread when needed. The class is designed to facilitate SPI communication within the broader control and interface module.
"""

import sys
import threading
from time import sleep
import json
import RPi.GPIO as gpio

#------ RPI 4 Pins ------
# SCLK = 11
# CS0  = 8
# CS1  = 7
# CS2  = 6
# MOSI = 10
# MISO = 9
#------------------------


class iface_handler:
    def __init__(self, fs, SCLK, CS0, CS1, CS2, MOSI, MISO):
        # ------------ Pin ------------
        self.SCLK = SCLK
        self.CS   = CS0  # Default CS0
        self.MOSI = MOSI
        self.MISO = MISO
        # ----------- Setup -----------
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        gpio.setup(SCLK, gpio.OUT)  # SCLK
        gpio.setup(CS0, gpio.OUT)   # CS0
        gpio.setup(CS1, gpio.OUT)   # CS1
        gpio.setup(CS2, gpio.OUT)   # CS2
        gpio.setup(MOSI, gpio.OUT)  # MOSI
        gpio.setup(MISO, gpio.IN)   # MISO
        # ------ Initialize pins ------
        gpio.output(CS0, gpio.HIGH)
        gpio.output(CS1, gpio.HIGH)
        gpio.output(CS2, gpio.HIGH)
        gpio.output(MOSI, gpio.LOW)
        # --------- Variables ---------
        self.data_out = []
        self.data_in = []
        self.clk_enable = True
        self.read_enable = False
        self.response = None
        self.ts = 1 / (2 * fs)
        self.BTM_MAPPING = self.load_mapping('btm_mapping.json')
        self.VELM_MAPPING = self.load_mapping('velm_mapping.json')
        self.SAM_MAPPING = self.load_mapping('sam_mapping.json') 

    # Thread for slave clock
    def spi_clk(self):
        while self.clk_enable:
            gpio.output(self.SCLK, gpio.HIGH)
            if self.read_enable:
                self.master_in()
            sleep(self.ts)
            gpio.output(self.SCLK, gpio.LOW)
            try:
                self.master_out()
                gpio.output(self.CS, gpio.LOW)
                self.read_enable = True
            except:
                gpio.output(self.CS, gpio.HIGH)
                gpio.output(self.MOSI, gpio.LOW)
                self.read_enable = False
                self.fetch_data()
            sleep(self.ts)
        # gpio.cleanup()

    # Read in Master In, Slave Out
    def master_in(self):
        if gpio.input(self.MISO):
            self.data_in.append(1)
        else:
            self.data_in.append(0)

    # Write in Master Out, Slave In
    def master_out(self):
        gpio.output(self.MOSI, self.data_out.pop(0))

    # Fetch data from MISO, list to int
    def fetch_data(self):
        bit_count = 0
        data = 0
        if len(self.data_in) == 32:
            while bit_count < 32:
                bit_state = self.data_in.pop(0)
                data <<= 1
                data |= bit_state
                bit_count += 1
            self.response = data

    # Set the queue and send the data by MOSI, int to list
    def send_data(self, data_to_send):
        bit_count = 0
        queue_to_send = []
        while bit_count < 32:
            queue_to_send.insert(0, data_to_send & 1)
            data_to_send >>= 1
            bit_count += 1
        self.data_out = queue_to_send  # Send the data

    # Create and start the clock thread
    def start_clk(self):
        sclk_thread = threading.Thread(target=self.spi_clk)
        sclk_thread.start()

    def get_data(self):
        data = self.response
        self.response = None
        return data

    def change_device(self, device):
        self.CS = device

    def kill_spi(self):
        self.clk_enable = False

    #Load mapping for the MODE of the 32 bit command
    def load_mapping(self, mapping_file):
        with open(mapping_file, 'r') as file:
            return json.load(file)
        

    def construct_spi_bits(self, mode, module, values):
        """
        Constructs a 32-bit SPI command based on the operation mode, module, and values.

        Parameters:
        - mode: 'read' or 'write'
        - module: 'SAM', 'VELM', or 'BTM'
        - values: A dictionary containing specific values for the command fields.

        Returns:
        - A 32-bit integer representing the SPI command.
        """
        spi_bits = 0

        # Set the read/write bit (bit 31)
        if mode == 'write':
            spi_bits |= 1 << 31  # Set bit 31 to 1 for write mode

        # Set the module bits (bit 30 to 28)
        if module == 'SAM':
            spi_bits |= 0b001 << 28
        elif module == 'VELM':
            spi_bits |= 0b010 << 28
        elif module == 'BTM':
            spi_bits |= 0b100 << 28

        spi_bits |= (values.get('error', 0) & 0xF) << 24
        spi_bits |= (values.get('voltage', 0) & 0xFF) << 16
        spi_bits |= (values.get('current', 0) & 0xFF) << 8
        spi_bits |= values.get('power', 0) & 0xFF

        return spi_bits
