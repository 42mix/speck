from speck.speck import Speck
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root=Tk()
root.title('entry box on canvas')
root.geometry('323x576')
#make sure app cant be resized
root.resizable(width=False, height="false")

#define bg img
bg= ImageTk.PhotoImage(file='C:/Users/nevin/OneDrive/Pictures/beach.png')

#define canvas
my_canvas= Canvas(root, width=323, height=576,bd=0,highlightthickness=0)
my_canvas.pack(fill="both",expand=True)

#put img on canvas
my_canvas.create_image(0,0,image=bg, anchor="nw")

#def entry boxes

un_entry= Entry(root,font=("Helvetica",24), width=14, fg="dark blue",bd=0)
pw_entry= Entry(root,font=("Helvetica",24), width=14, fg="dark blue",bd=0)

un_entry.insert(0,"username")
pw_entry.insert(0,"password")

#def entry_clear func
def entry_clear(e):
    if un_entry.get()=="username" or pw_entry.get()=='password':
        un_entry.delete(0,END)
        pw_entry.delete(0,END)
        #change pw to ***
        pw_entry.config(show='*')

#bind the entry boxes, ie when you click it, the text on input box shd vanish
un_entry.bind("<Button-1>",entry_clear)
pw_entry.bind("<Button-1>",entry_clear)


#add entry boxes to canvas
un_window= my_canvas.create_window(34,290, anchor='nw', window=un_entry)
pw_window= my_canvas.create_window(34,370, anchor='nw', window=pw_entry)

def new_window():
    _list = root.winfo_children()

    for item in _list :
        if item.winfo_children() :
            for i in item.winfo_children():
                i.pack_forget()

    #bottom= Toplevel()
    #bottom.geometry("400x400")
    lbl= Label(root, text="NOICE world").pack()
    btn2=Button(root, text="close window", command=root.destroy).pack()
    

#create welcome screen
def destroy(root,func):
    root.destroy()
    func()

def welcome():
    if un_entry.get()=="username" or pw_entry.get()=='password' or un_entry.get()=="" or pw_entry.get()=='':
        response=messagebox.showwarning("ERROR","ENTER USERNAME AND PASSWORD")
    elif un_entry.get()!="11C" or pw_entry.get()!='11c2021':
        response=messagebox.showwarning("ERROR","ENTER CORRECT USERNAME AND PASSWORD")
    

    else:
        un_entry.destroy()
        pw_entry.destroy()
        login_btn.destroy()
        my_canvas.destroy()
        #root.destroy()
        '''top= Toplevel()
        top.title('this is a new window')'''
        root.geometry("400x400")
        lbl= Label(root, text="hello world").pack()
        btn2=Button(root, text="close window", command=root.destroy).pack()
        btn3=Button(root, text="create window", command=new_window).pack()
    '''def inner():
        if un_entry.get()=="username" or pw_entry.get()=='password' or un_entry.get()=="" or pw_entry.get()=='':
            response=messagebox.showwarning("ERROR","ENTER USERNAME AND PASSWORD")
        elif un_entry.get()!="11C" or pw_entry.get()!='11c2021':
            response=messagebox.showwarning("ERROR","ENTER CORRECT USERNAME AND PASSWORD")
    

        else:
            un_entry.destroy()
            pw_entry.destroy()
            login_btn.destroy()
            my_canvas.destroy()
            root.destroy()
        

        #add a welcome message
            top= Toplevel()
            top.title('this is a new window')
            top.geometry("400x400")
            lbl= Label(top, text="hello world").pack()
            btn2=Button(top, text="close window", command=top.destroy).pack()
            btn3=Button(top, text="create window", command=welcome).pack()
    top.destroy()
    inner()'''
        

#def btn
login_btn= Button(root, text="LOGIN",font=("Helvetica",20), width=15,fg="dark blue", command=welcome)
login_btn_window= my_canvas.create_window(36,470, anchor='nw', window=login_btn)

with open("token.txt",'r') as f:
    speck=Speck(f.read().rstrip())



















    
