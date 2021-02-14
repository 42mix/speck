from tkinter import *

root=Tk()
root.title('aahhhh')

r=IntVar() #integer variable, if value was a string then it will be StrVar()
r.set('2') #will always display 2 under the options
def clicked(value):
    mylabel= Label(root, text=value)
    mylabel.pack()
    

Radiobutton(root, text="Option1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
#lambda is used as it has to get the value(not sure)
#when a radiobutton is clicked, the value will go to the function and update the label
mylabel= Label(root, text=r.get())
mylabel.pack()

myButton= Button(root, text="click me", command=lambda: clicked(r.get()))
myButton.pack()
mainloop()

