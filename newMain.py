from Tkinter import *
import Tkinter as tk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.widgets()
        self.master.title("Finder wants to make changes.")

    def widgets(self):
        okayButton = Button(self, text="Okay")
        okayButton.grid(row=1, column=1)




def start():
    root = Tk()
    root.grid()
    app = Window(root)
    root.mainloop()

start()
