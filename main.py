import tkinter as tk
import connect as con
import login_super as super
root=tk.Tk()
root.title("Main")
root.geometry('1366x768')
image=tk.PhotoImage(file="main_back.png")
imagelabel=tk.Label(root,image=image,borderwidth=0)
imagelabel.pack(fill="both")


def func():
    con.fun(root)

def func1():
    super.fun(root)

img=tk.PhotoImage(file="Group 12.png")
button1=tk.Button(imagelabel,image=img,borderwidth=0,activebackground="#ffffff",command=func)
button1.place(x=200,y=600)

imgo=tk.PhotoImage(file="Group 12.png")
button2=tk.Button(imagelabel,image=imgo,borderwidth=0,activebackground="#ffffff",command=func1)
button2.place(x=850,y=600)

root.mainloop()