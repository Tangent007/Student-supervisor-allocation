# import tkinter as tk
from tkinter import *
import sqlite3
import super_details as sup
import tkinter.messagebox
import signup_super as super
logon=sqlite3.connect("stud_details.db")
log=logon.cursor()

def fun(root):
    
    global home
    root.withdraw()

    home = Toplevel()

    root.resizable(0, 0)


    home.title("login_supervisor")
    home.geometry("1366x768")
    image=PhotoImage(file="log_sup.png")
    imagelabel=Label(home,image=image,borderwidth=0)
    imagelabel.pack(fill="both")


    # ------user entered values----------

    user=Entry(imagelabel)
    user.place(x=800,y=310)


    var=StringVar(root)
    max_len=9
    def on_write(*args):
        s=var.get()
        if len(s)> max_len:
            var.set(s[:max_len])
    var.trace_variable("w",on_write)





    # func of login
    def log_in():
        
        name1=user.get()
        passwo=passw.get()
        # disp=tk.Text(master=root,height=10,width=30)
        # disp.place(x=30,y=30)
        # disp.insert(tk.END,name1)
        log.execute("select * from super_details where Name=? and password=?",(name1,passwo,))
        d=log.fetchone()
        if d is not None:
            sup.func(home,name1,passwo,d)
        else:
            # print('Login failed')
            tkinter.messagebox.showwarning("False Login" , "please try again")

    passw=Entry(imagelabel,show="*",textvariable=var)
    passw.place(x=800,y=380)
    
    # func of sign up
    def sign_up():
        super.func(home)

    # login label link

    logo=PhotoImage(file="Group 6.png")
    logo1=Button(home,image=logo,borderwidth=0,bg="#ffffff",activebackground="#ffffff",command=log_in)
    logo1.place(x=650,y=500)


    # sign up label link
    logo2=PhotoImage(file="Group 5 (2).png")
    logo3=Button(home,image=logo2,borderwidth=0,bg="#6AB7FF",activebackground="#6AB7FF",command=sign_up)
    logo3.place(x=302,y=400)


    root.mainloop()