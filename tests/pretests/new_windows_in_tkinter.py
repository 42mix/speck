from tkinter import *

root=Tk()
root.title("new window")


def open():
    top= Toplevel()
    top.title('this is a new window')
    lbl= Label(top, text="hello world").pack()
    btn2=Button(top, text="close window", command=top.destroy).pack() 


btn=Button(root, text="open 2nd window", command=open).pack()


mainloop()
