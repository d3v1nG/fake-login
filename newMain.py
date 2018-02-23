#for 2.7.10
from Tkinter import *
#import Tkinter as Tk

#for 3.6.4
#from tkinter import *
#import tkinter as tk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.widgets()
        self.entry()
        self.master.title("Finder wants to make changes.")

#Button functions (this dont work yet)
    def okay(user):
        tries = 0
        userName = user.get()
        print("User Name: " + userName)


    def exitButton(self):
        exit()

#Widgets and Entries
    def widgets(self):
        okayButton = Button(self, text="Okay", command=self.okay)
        okayButton.grid(row=5, column=1)

        cancelButton = Button(self, text="Cancel", command=self.exitButton)
        cancelButton.grid(row=5, column=2)

    def entry(self):
        user = StringVar()

        L1 = Label(self, text="User Name")
        L1.grid(row=2, column=1)
        E1 = Entry(self, bd =5, textvariable=user)
        E1.grid(row=2, column=2)

        return user


#Starts the program
def start():
    master = Tk()
    app = Window(master)
    master.mainloop()

start()
