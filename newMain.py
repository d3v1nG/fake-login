
#for 3.6.4
from tkinter import *
import tkinter as tk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.widgets()
        self.entry()
        self.master.title("Finder wants to make changes.")

#Button functions (this dont work yet)
    def okay():
        print(E1.get())

#Widgets and Entries
    def widgets(self):
        okayButton = Button(self, text="Okay", command=okay())
        okayButton.grid(row=5, column=1)

        cancelButton = Button(self, text="Cancel")
        cancelButton.grid(row=5, column=2)

    def entry(self):
        L1 = Label(self, text="User Name")
        L1.grid(row=2, column=1)
        E1 = Entry(self, bd =5)
        E1.grid(row=2, column=2)

#Starts the program
def start():
    root = Tk()
    root.grid()
    app = Window(root)
    root.mainloop()

start()
