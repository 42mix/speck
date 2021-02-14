from tkinter import *
root = Tk()
def myclick():
    myLabel= Label(root,text="I clicked IT!")
    myLabel.pack()


myButton = Button(root, text="click ME!",padx=50, command= myclick,fg='blue',bg="light blue")
'''if you do command =myclick(), ie u put () after, they will display the text
here its i clicked IT! before you click the button
fg="any color" changes text color insidebutton and bg='any color' changes background color of the button color'''
#command= goes to the function

#padx and pady increases length and width along x and y axis resp
#DISABLED disables the button ie you cannot click it
myButton2 = Button(root, text="click ME!", pady=50,state=DISABLED)
myButton.pack()
myButton2.pack()
root.mainloop()
