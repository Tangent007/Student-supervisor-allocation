# import tkinter as tk
from tkinter import *
import sqlite3
import tkinter.messagebox
import connect as con
signup=sqlite3.connect("stud_details.db")
sign=signup.cursor()

def func(root):
    
    global next

    root.withdraw()

    next = Toplevel()

    root.resizable(0, 0)

    var=StringVar(root)
    max_len=9
    def on_write(*args):
        s=var.get()
        if len(s)> max_len:
            var.set(s[:max_len])
    var.trace_variable("w",on_write)


    next.title("signup_student")
    next.geometry("1366x768")
    image=PhotoImage(file="signup_stude.png")
    imagelabel=Label(next,image=image,borderwidth=0)
    imagelabel.pack(fill="both")


    # func to enter student details in database

    def edetails():
        # sign.execute("create table login_details(Name text,Reg_No number,Specialization text,Mobile_no text,Email_id text,password number)")
        n=str(name.get())
        r=int(reg.get())
        s=str(specialization.get())
        m=str(mobile.get())
        e=str(email.get())
        p=int(password.get())
        sign.execute("insert into login_details values(?,?,?,?,?,?)",(n,r,s,m,e,p))
        e=sign.fetchone()
        print(e)
        # d=sign.execute("select * from login_details where password=?",(p,))
        # for x in d:
        #     print(x)
        # if (n is None or r is None or s is None or m is None or e is None or p is None):
        #     tkinter.messagebox.showwarning("not enough data","enter all fields")
        signup.commit()
        logg()

    # func of login button
    def logg():
        con.fun(next)



    # ---------user entered details section-------------

    name=Entry(next)
    name.place(x=900,y=200)

    reg=Entry(next)
    reg.place(x=900,y=250)

    specialization=Entry(next)
    specialization.place(x=900,y=300)

    mobile=Entry(next)
    mobile.place(x=900,y=360)

    email=Entry(next)
    email.place(x=900,y=410)

    password=Entry(next,textvariable=var)
    password.place(x=900,y=460)



    # login label link

    logo=PhotoImage(file="login_sup.png")
    logo1=Button(next,image=logo,borderwidth=0,command=logg)
    logo1.place(x=350,y=380)

    # sign up label link
    logo2=PhotoImage(file="Group 7.png")
    logo3=Button(next,image=logo2,borderwidth=0,bg="#ffffff",activeforeground="#ffffff",activebackground="#ffffff",command=edetails)
    logo3.place(x=790,y=500)

    next.mainloop()