import time
from tkinter import *

def circle(win, x, y, r):
    win.plot(x, y, "red")
    r2 = r * r
    check = r + 1
    until_check2 = 4000000000
    for a in range(1, int(r / 1.41) + 1): #calc coordinates down to sqrt(2)/2
        diff = r2 - (a * a)
        if diff < until_check2:
            check -= 1 #set point of next lower pixel coordinate
            until_check2 = ((check * check) + ((check - 1) * (check - 1))) / 2 # calculate next threshold
        b = check # keep last until threshold reached
        win.plot(x + a, y - b, "blue") # calculate 1/8 of all points and mirror the rest
        win.plot(x + a, y + b, "blue")
        win.plot(x + b, y - a, "blue")
        win.plot(x + b, y + a, "blue")
        win.plot(x - a, y - b, "blue")
        win.plot(x - a, y + b, "blue")
        win.plot(x - b, y - a, "blue")
        win.plot(x - b, y + a, "blue")

master = Tk()
master.title("Draw a circle")
can = Canvas(master, width = 300, height = 300)
can.pack(expand = YES, fill = BOTH)

class Win:
    def __init__(self, can):
        self.can = can
    def plot(self, x, y, c):
        self.can.create_line(x, y, x + 1, y, fill = c)

win = Win(can)
s = time.time()
circle(win, 150, 150, 120)

print(time.time() - s, "seconds..")

mainloop()