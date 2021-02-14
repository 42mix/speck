from tkinter import *

root=Tk()
root.title('sliders')
root.geometry("400x400") #increases size of window ie horizontal x vertical

#dropdown boxes
clicked = StringVar() #since str are used[monday,tue........]
clicked.set("monday")#default

def show():
    myLabel=Label(root, text=clicked.get()).pack()

drop=OptionMenu(root, clicked, "monday","tuesday","wednesday","thursday","friday")
drop.pack()
#clicked is a variable, can be any variable

mybtn=Button(root, text= "show chosen day", command=show).pack()



root.mainloop()
