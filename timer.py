import tkinter as tk
from tkinter.constants import *


class Timer:
    def __init__(self, root, hours, minutes, seconds):
        self.root = root
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.clock = tk.Label(self.root, height=1, background="#000000", foreground='white', font=("Lemon Milk", 20),
                              anchor=CENTER, text="00:00:00")
        self.clock.place(relx=0.5, rely=0.5, anchor=CENTER)

    def start_clock(self):
        print("worked")
        if self.hours == 4:
            return  # Stop timer

        self.seconds -= 1
        if self.seconds == 00:
            self.minutes -= 1
            self.seconds = 60

        if self.minutes == 00 and self.seconds == 00:
            self.hours += 1

    def run(self):
        self.clock.config(text=f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}')
        self.root.after(1000, self.start_clock)  # Call again in 1 seconds (1000ms)
