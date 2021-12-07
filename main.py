#this project is for learning tkinter and creating guis for my other projects

#importing tkinter module
from tkinter import *

root = Tk()

#creating a Label Widget
myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="My Name Is John Elder").grid(row=1, column=0)

#shoving it onto the screen
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=0)

root.mainloop()