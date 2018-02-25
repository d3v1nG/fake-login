from tkinter import *
root = Tk()
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
img = PhotoImage(file="./Images/finder.png")
canvas.create_image(5,5, anchor=NW, image=img)
mainloop()
