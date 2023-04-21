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

#spi_bus = 0
#spi_dev = 0
#spi_max = 250000

def set_spi(bus,dev,hz):
    spi = spidev.SpiDev()
    spi.open(bus,dev)
    spi.max_speed_hz = hz
    return spi

def check_spi():
    spi.writebytes([])
    sleep(0.1)
    spi.readbytes([])


def send_cmd(cmd):
    try:
        while True:
            spi.writebytes([cmd])
            sleep(0.1)
        
    finally:
        spi.close()




spi = set_spi(0,0,7629)
send_cmd(0x3)

