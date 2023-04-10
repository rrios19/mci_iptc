# Tecnologico de Costa Rica
# Integrated Power Test system for CubeSats (IPTC)
# Control and Interface Module
# Author: Ronald Rios
# Description: SPI interface
# --------   MOSI,MISO   ---------
# | RPI4 | <-----------> | STM32 |
# --------    SCLK,SS    ---------

import spidev
from time import sleep

spi_bus = 0
spi_dev = 1
spi_max = 250000

def init_spi(bus,dev,hz):
    spi = spidev.SpiDev()
    spi.open(bus,dev)
    spi.max_speed_hz = hz

def send_cmd():
    try:
        while True:
            spi.writebytes([0x3A])
            sleep(0.1)
        
    finally:
        spi.close()

