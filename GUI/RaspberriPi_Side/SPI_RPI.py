import spidev
import RPi.GPIO as GPIO
import json

# Set up GPIO for the CS lines
CS_PINS = [8, 7, 6]  # CS0, CS1, CS2
GPIO.setmode(GPIO.BCM)
for pin in CS_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)  # Set CS high initially

# Create a SpiDev object
spi = spidev.SpiDev()

# Open the SPI device
spi.open(0, 0)  # The CS parameter doesn't matter as we're handling it manually

# Set SPI speed and mode
spi.max_speed_hz = 500000
spi.mode = 0

def send_instruction(instructionsPath):
    BTM = CS_PINS[0]
    SAM = CS_PINS[1]
    VELM = CS_PINS[2]
    ModulePins = {"BTM":BTM,"SAM":SAM,"VELM":VELM}

    instructions = load_instructions(instructionsPath)

    for InstType in instructions:
        if InstType in ModulePins:
            cs_pin = ModulePins[InstType]

            # Pull the CS line low
            GPIO.output(cs_pin, GPIO.LOW)

            syncInst = instructions["sync"]

            # Send the sync instruction
            bytes_out = [(syncInst >> i) & 0xff for i in (24, 16, 8, 0)]
            spi.xfer(bytes_out)
            print("Transferred", syncInst)

            # Receive the reply
            reply_bytes = spi.readbytes(4)  # Read 4 bytes for a 32-bit reply

            # Convert the reply bytes to a 32-bit integer
            reply = 0
            for byte in reply_bytes:
                reply = (reply << 8) | byte

            if reply == instructions['syncreply']:
                for moduleInst in instructions[InstType]:
                    # Convert the instruction to a list of bytes
                    bytes_out = [(moduleInst >> i) & 0xff for i in (24, 16, 8, 0)]
            
                    # Send the bytes
                    spi.xfer(bytes_out)

                # Pull the CS line high
                GPIO.output(cs_pin, GPIO.HIGH)


def receive_word():
    # Receive four bytes
    bytes_in = spi.readbytes(4)

    # Combine the four bytes into a 32-bit word
    word = 0
    for byte in bytes_in:
        word = (word << 8) | byte

    return word



# Now you can send an instruction to each STM32 with:
# send_instruction(your_instruction, CS_PINS[0])  # For STM32 connected to CS0
# send_instruction(your_instruction, CS_PINS[1])  # For STM32 connected to CS1
# send_instruction(your_instruction, CS_PINS[2])  # For STM32 connected to CS2

def load_instructions(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

try:
    # Now you can receive data from each STM32 with:
    data0 = send_instruction("IPTC/TestingWorkspace/tests/seqInstruction.json")  # For STM32 connected to CS0
finally:
    GPIO.cleanup()  # This ensures all GPIOs are reset when the script ends

# data1 = receive_data(CS_PINS[1])  # For STM32 connected to CS1
# data2 = receive_data(CS_PINS[2])  # For STM32 connected to CS2