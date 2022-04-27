import tkinter as tk
from tkinter.constants import *


class Timer:
    def __init__(self, root, hours, minutes, seconds, clock):
        self.root = root
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.clock = clock
        self.clock.place(x=70, y=400)

    def start_clock(self):
        if self.hours == 0 and self.minutes == 0 and self.seconds == 1:
            return  # Stop timer

        self.seconds -= 1
        if self.seconds == 00:
            self.minutes -= 1
            self.seconds = 60

        if self.minutes == 00 and self.seconds == 00:
            self.hours += 1

        self.clock.config(text=f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}')
        self.root.after(1000, self.start_clock)  # Call again in 1 seconds (1000ms)
