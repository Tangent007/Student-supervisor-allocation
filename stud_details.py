from tkinter import *
import sqlite3

stud=sqlite3.connect("stud_details.db")
stu=stud.cursor()

def func(root,d,name,passw):
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

    root.title("student details")
    root.geometry("1366x768")
    imo=PhotoImage(file="stu_back.png")
    imag=Label(Home,image=imo,borderwidth=0)
    imag.pack(fill="both")

    # student login after details

    def stu_part():
        stu.execute("select * from login_details where Name=? and password=?",(name,passw,))
        d=stu.fetchone()
        if d is not None:
            print(d[0])
            # print("\n")
            print(d[1])
            # print("\n")
            print(d[2])
            # print("\n")
        # tb=tk.Text(root,text="name")
        # tb.pack()
        details='Name : '+d[0]+'\n'+'\n'+'Reg no. : '+str(d[1])+'\n'+'\n'+'Specialization : '+d[2]
        disp=Text(master=Home,height=10,width=30,bg="#ECECEC",borderwidth=0)
        disp.place(x=200,y=300)
        disp.insert(END,details)


    def logout():
        exit(0)

    # spervisor ka details

    def super_dt():


        # drop down to select specialization
        varia=StringVar(Home)
        varia.set("C")
        drop=OptionMenu(Home,varia,"C","C++","Python")
        drop.place(x=600,y=200)

        print(d[2])

        stu.execute("select * from super_details where Specialization=?",(d[2],))
        a=stu.fetchall()
        print(a)
        for x in a:
            detail='  '+str(x[1])+'\t\t\t'+x[0]+'\n'
            displ=Text(master=Home,height=20,width=85,bg="#ffffff",borderwidth=0)
            displ.place(x=610,y=300)
            displ.insert(END,detail)



    button1=Button(Home,text="exit",command=logout)
    button1.place(x=100,y=550)



    # user='Tanuj'
    # passw='123456789'
    stu_part()
    super_dt()


    Home.mainloop()