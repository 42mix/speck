from tkinter import *
root = Tk()
#creating a Label Widget
myLabel1= Label(root, text="hello world!").grid(row=0, column=0)
myLabel2= Label(root, text="My name is Nevin Jose").grid(row=1, column=5)
#shoving it on the screen--> myLabel.pack()
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=0)
root.mainloop()
