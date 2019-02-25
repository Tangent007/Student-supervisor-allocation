# import tkinter as tk
from tkinter import *
import sqlite3
import tkinter.messagebox
import signup_stu as student
import stud_details as stud
def fun(root):
    
    global Home
    root.withdraw()

    Home = Toplevel()

    root.resizable(0, 0)

    logd=sqlite3.connect("stud_details.db")
    logon=logd.cursor()


    var=StringVar(root)

    Home.title("login_student")
    Home.geometry("1366x768")
    image=PhotoImage(file="home.png")
    imagelabel=Label(Home,image=image,borderwidth=0)
    imagelabel.pack(fill="both")

    # func of login

    # def log():
    #     stud.func(Home)

    def use():
        name1=userl.get()
        passw=pass1.get()
        # disp=tk.Text(master=root,height=10,width=30)
        # disp.place(x=30,y=30)
        # disp.insert(tk.END,name1)
        logon.execute("select * from login_details where Name=? and password=?",(name1,passw,))
        d=logon.fetchone()
        if d is not None:
            stud.func(Home,d,name1,passw)
        else:
            # print('Login failed')
            tkinter.messagebox.showwarning("False Login" , "please try again")


    # func of sign up

    def sign():
        student.func(Home)

        

    # user entry box

    userl=Entry(imagelabel)
    # userl.config(width=20,height=20)
    userl.place(x=440,y=280)
    # print(userl.get())

    # password entry box

    max_len=9
    def on_write(*args):
        s=var.get()
        if len(s)> max_len:
            var.set(s[:max_len])
    var.trace_variable("w",on_write)

    pass1=Entry(imagelabel,show="*",textvariable=var)
    pass1.place(x=440,y=330)

    # login label link

    logo=PhotoImage(file="Group 72.png")
    logo1=Button(Home,image=logo,borderwidth=0,bg="#E8E8E8",command=use)
    logo1.place(x=500,y=380)



    # sign up label link
    logo2=PhotoImage(file="Group 82.png")
    logo3=Button(Home,image=logo2,borderwidth=0,bg="#E8E8E8",activebackground="#E8E8E8",command=sign)
    logo3.place(x=430,y=624)
    Home.mainloop()


    # def run():
    #     s1.runn()


    # root.mainloop()



# def Back():
#     Home.destroy()
#     root.deiconify()