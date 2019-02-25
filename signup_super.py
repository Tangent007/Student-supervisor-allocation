from tkinter import *
import sqlite3
import tkinter.messagebox
import login_super as super

signd=sqlite3.connect("stud_details.db")
signsup=signd.cursor()

def func(root):
        global Home
        root.withdraw()

        Home = Toplevel()

        root.resizable(0, 0)

        var=StringVar(Home)
        max_len=9
        def on_write(*args):
               s=var.get()
               if len(s)> max_len:
                   var.set(s[:max_len])
        var.trace_variable("w",on_write)

        Home.title("signup_supervisor")
        Home.geometry("1366x768")
        image=PhotoImage(file="signsuper.png")
        imagelabel=Label(Home,image=image,borderwidth=0)
        imagelabel.pack(fill="both")



        # func to enter student details in database

        def edetails():
                # signsup.execute("create table super_details(Name text,UID number,Specialization text,Mobile_no text,Email_id text,password number)")
                n=str(name.get())
                r=int(uid.get())
                s=str(specialization.get())
                m=str(mobile.get())
                e=str(email.get())
                p=int(password.get())
                signsup.execute("insert into super_details values(?,?,?,?,?,?)",(n,r,s,m,e,p))
                # d=signsup.execute("select * from super_details",p)
                # for x in d:
                #         print(x)
                # signsup.execute("delete from super_details where Name=?",('J',))
                signd.commit()
                log_in()


        # ---------user entered details section-------------

        name=Entry(Home)
        name.place(x=900,y=200)

        uid=Entry(Home)
        uid.place(x=900,y=250)

        specialization=Entry(Home)
        specialization.place(x=900,y=300)

        mobile=Entry(Home)
        mobile.place(x=900,y=360)

        email=Entry(Home)
        email.place(x=900,y=410)

        password=Entry(Home,textvariable=var)
        password.place(x=900,y=460)





        # func after clicking on image
        def log_in():
                super.fun(Home)



        # binding image with func



        # login label link

        logo=PhotoImage(file="login_sup.png")
        logo1=Button(Home,image=logo,borderwidth=0,command=log_in)
        logo1.place(x=350,y=380)



        # sign up label link
        logo2=PhotoImage(file="Group 7.png")
        logo3=Button(Home,image=logo2,borderwidth=0,bg="#ffffff",activebackground="#ffffff",command=edetails)
        logo3.place(x=790,y=500)



        root.mainloop()