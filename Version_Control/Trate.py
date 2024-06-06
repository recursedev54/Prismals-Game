# Version_Control/Trate.py

from Time.init_time import global_time
import time

class Trate:
    def __init__(self, initial_time=1):
        self.time = initial_time

    def start(self):
        while True:
            self.time += 2
            global_time.update_time(1)
            time.sleep(1)

trate = Trate()
