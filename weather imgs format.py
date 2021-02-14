from tkinter import *
#PIL-Python Image Library
from PIL import ImageTk,Image
root= Tk()
root.title("welcome to weather forecast")

#root.iconbitmap('http://openweathermap.org/img/wn/{icon}.png')

button_quit= Button(root, text="exit program", command= root.quit)
#ends the program when clicked
button_quit.pack()








root.mainloop()
#the feather or any img on the top left of output is called an icon
