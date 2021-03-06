from tkinter import *
root = Tk()
root.title('simple calculator')

e= Entry(root, width=35, borderwidth=10)
e.grid(row=0,column=0,columnspan=3, padx=10, pady=10)
def button_click(number):
    #e.delete(2,END)
    #e.delete() clears the entire space after clicking a digit,if not there you can type infinite no of digits
    #the no on left of end shows no of digits to be displayed, ie 0 means display 1 dig, 1 means display 2 and so on
    e.insert(0, number) #gives no in reverse
#define buttons

button_1= Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1)).grid(row=3, column=0)
button_2= Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2)).grid(row=3, column=1)
button_3= Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3)).grid(row=3, column=2)

button_4= Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4)).grid(row=2, column=0)
button_5= Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5)).grid(row=2, column=1)
button_6= Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6)).grid(row=2, column=2)

button_7= Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7)).grid(row=1, column=0)
button_8= Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8)).grid(row=1, column=1)
button_9= Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9)).grid(row=1, column=2)

button_0= Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0)).grid(row=4, column=0)

button_add= Button(root,text="+",padx=39, pady=20, command=lambda: button_click()).grid(row=5, column=0)
button_equal= Button(root,text="=",padx=91, pady=20,command=lambda: button_click()).grid(row=5, column=1,columnspan=2)
button_clear= Button(root,text="CLEAR",padx=79, pady=20, command=lambda: button_click()).grid(row=4, column=1, columnspan=2)

#put buttons on screen


root.mainloop()