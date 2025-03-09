import time
from tkinter import *
from tkinter.ttk import *

class Window(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.Widgets()

    def Widgets(self):
        self.label = Label(self, text = "Pomodoro Timer")
        self.label.grid(row = 0, column = 0)

def focus():
    t = 1500

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Break time")

def rest():
    t = 300

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Focus time")

def main():
    app = Window(None)
    app.mainloop()
    

if __name__ == "__main__":
    main()