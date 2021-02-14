from tkinter import *
root = Tk()

e= Entry(root, width=50, borderwidth=10)
e.pack()
e.insert(0,"enter your name:")
#insert shows the statement within the input box
#Entry() is the entry widget in which the user can input data

#e.get() func gets whatever the user types into the input box
'''def myclick():
    myLabel= Label(root,text="hello " + e.get())
    myLabel.pack()             or'''
def myclick():
    hello= 'hello ' + e.get()
    myLabel= Label(root,text= hello)
    myLabel.pack()


myButton = Button(root, text="Enter Your Name:",padx=50, command= myclick,fg='blue',bg="light blue")
myButton.pack()

root.mainloop()
