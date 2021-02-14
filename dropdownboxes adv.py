from tkinter import *

root=Tk()
root.title('sliders')
root.geometry("400x400") #increases size of window ie horizontal x vertical

#dropdown boxes

def show():
    myLabel=Label(root, text=clicked.get()).pack()

options=[
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday"
    ]



clicked = StringVar() #since str are used[monday,tue........]
clicked.set(options[0])#default


drop=OptionMenu(root, clicked,*options)
drop.pack()
#clicked is a variable, can be any variable

mybtn=Button(root, text= "show chosen day", command=show).pack()



root.mainloop()
