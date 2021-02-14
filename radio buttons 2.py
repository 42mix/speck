from tkinter import *



root=Tk()
root.title("radiobuttons")

TOPPINGS = [
    ("pepperoni","pepperoni"),
    ("cheese","cheese"),
    ("bacon","bacon"),
    ("pastrami","pastrami"),
    ]
pizza= StringVar()#intvar if the value was an int
pizza.set("pepperoni") #default value/option

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)#west

myLabel=Label(root,text="")
myLabel.pack()

def clicked(value):
    myLabel.config(text=value)

myButton=Button(root,text="click me!", command=lambda: clicked(pizza.get()))
myButton.pack()


    
mainloop()
