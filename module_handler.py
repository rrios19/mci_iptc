# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and Interface Module
# Author: Ronald Rios
# Description: Module thread handler
# Usage: >>> instance_name = module_handler(pin)

import threading

class module_handler:
    def __init__(self,inst):
        self.inst = inst    # Instrument identifier/ It can't be changed
        self.test_time = 0  # Default 0, means start and stop immediately
        self.wait_time = [] # Wait time for each setting
        self.cmmd_list = [] # Command list
        self.ready_cmd = [] # Command ready for send
        self.WCLK = None    # Hold clock
        self.TCLK = None    # Test clock

    # Configure test time/ If the time isn't set, the test will stop immediately
    def conf_time(self,time):
        self.test_time = int(time)

    # Append a hold time/time interval
    def append_wait(self,wait):
        self.wait_time.append(int(wait))

    # Append a command
    def append_cmd(self,cmd):
        self.cmmd_list.append(int(cmd))

    # Pop the first ready command
    def pop_ready(self):
        return self.ready_cmd.pop(0) if self.ready_cmd else False

    # Return the instrument pin/identifier
    def get_inst(self):
        return self.inst

    # Waits for some time and then puts the command in a queue with its identifier
    def wait_clk(self):
        if self.wait_time and self.cmmd_list:
            time = self.wait_time.pop(0)
            cmmd = self.cmmd_list.pop(0)
            self.ready_cmd.append(cmmd)
        else:
            time = 0
        self.WCLK = threading.Timer(time,self.wait_clk)
        self.WCLK.start()

    # Waits fot the test to finish and then kills the thread
    def test_clk(self):
        self.TCLK = threading.Timer(self.test_time,self.kill_wait)
        self.TCLK.start()

    # Starts both threads
    def start_test(self):
        self.wait_clk()
        self.test_clk()

    # Checks if the thread is alive
    def check_th(self):
        return self.TCLK.is_alive()

    # Stop the thread
    def kill_wait(self):
        self.WCLK.cancel()

