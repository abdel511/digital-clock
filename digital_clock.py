import sys
from tkinter import *
import time

def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text = time_string)
    clock.after(200,tick)
root= Tk()
clock = Label(root, font = ("time", 200, "bold"), bg = "green")
clock.grid(row = 0, column = 1)
tick()
root.mainloop()
