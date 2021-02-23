from tkinter import *

root=Tk()
root.title('sliders')
root.geometry("400x400") #increases size of window ie horizontal x vertical

def check():
    myLabel=Label(root,text= var.get()).pack()

var= StringVar()
c= Checkbutton(root, text="Check this Box.....I dare ya",variable=var, onvalue="YOU DID IT YOU CRAZY SON OF A BISH", offvalue="DIDNT THINK SO!")
c.deselect()
c.pack()

myButton= Button(root, text="show selection",command=check).pack()




root.mainloop()
