# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and Interface Module
# Author: Ronald Rios
# Description: Module thread handler
# Usage: >>> instance_name = module_handler()

import threading

class module_handler:
    def __init__(self):
        self.test_time = 0   # Default 0, means start and stop immediately
        self.interval_time = [] # Wait time for each command
        self.interval_cmd  = [] # Command list
        self.ready_cmd = [] # Command ready for send
        self.ICLK = threading.Timer(0,0) # Interval clock
        self.TCLK = threading.Timer(0,0) # Test clock

    # Configure test time/ If the time isn't set, the test will stop immediately
    def conf_time(self,time):
        self.test_time = int(time)

    # Append a wait time/time interval
    def append_time(self,interval):
        self.interval_time.append(int(interval))

    # Append a command
    def append_cmd(self,cmd):
        self.interval_cmd.append(int(cmd))

    # Pop the first ready command
    def pop_ready(self):
        return self.ready_cmd.pop(0) if self.ready_cmd else False

    # Waits for some time and then puts the command in a queue with its identifier
    def interval_clk(self):
        if self.interval_time and self.interval_cmd:
            time = self.interval_time.pop(0)
            cmd  = self.interval_cmd.pop(0)
            self.ready_cmd.append(cmd)
        else:
            time = 0
        self.ICLK = threading.Timer(time,self.interval_clk)
        self.ICLK.start()

    # Waits fot the test to finish and then kills the thread
    def test_clk(self):
        self.TCLK = threading.Timer(self.test_time,self.kill_interval)
        self.TCLK.start()

    # Starts both threads
    def start_test(self):
        self.interval_clk()
        self.test_clk()

    # Checks if the thread is alive
    def check_thread(self):
        return self.TCLK.is_alive()

    # Stop the thread
    def kill_interval(self):
        print("KILL MOD")
        self.ICLK.cancel()

