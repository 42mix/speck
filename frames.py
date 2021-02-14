from tkinter import*
root=Tk()
root.title("frames")

frame= LabelFrame(root,padx=50,pady=50)
frame.pack(padx=10, pady=10)
#you can add text on frame line by writing text="....."

def legend():
    print("you did it you crazy idiot!")
def lol():
    print("you just couldnt listen could ya?")

b=Button(frame, text="Dont Click Here!",command=lol)
b2=Button(frame, text= "or here!",command=legend)
b.grid(row=0,column=0)
b2.grid(row=1,column=1)

root.mainloop()
