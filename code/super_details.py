from tkinter import *
import sqlite3


sup=sqlite3.connect("stud_details.db")
supervisor=sup.cursor()


def func(root,user,passw,d):
        global Home
        root.withdraw()

        Home = Toplevel()

        root.resizable(0, 0)

        Home.title("supervisor details")
        Home.geometry("1366x768")
        img=PhotoImage(file="super_page.png")
        back=Label(Home,image=img,borderwidth=0)
        back.pack()

        def super_part():
                supervisor.execute("select * from super_details where Name=? and password=?",(user,passw,))
                d=supervisor.fetchone()
                if d is not None:
                        print(d[0])
                        # print("\n")
                        print(d[1])
                        # print("\n")
                        print(d[2])
                        # print("\n")
                        # tb=tk.Text(root,text="name")
                        # tb.pack()
                        details='Name : '+d[0]+'\n'+'\n'+'UID : '+str(d[1])+'\n'+'\n'+'Specialization : '+d[2]
                        disp=Text(master=Home,height=10,width=25,bg="#ffffff",borderwidth=0,font=("Sans-Serif",12))
                        disp.place(x=240,y=270)
                        disp.insert(END,details)

        #  func to show student details
        def student_dt():
                supervisor.execute("select * from login_details where Specialization=?",(d[2],))
                a=supervisor.fetchall()
                print(a)
                i=0
                for x in a:
                        
                        detail='  '+str(x[1])+'\t\t\t'+x[0]+'\n'
                        displ=Text(master=Home,height=10,width=75,bg="#ffffff",borderwidth=0)
                        displ.place(x=610,y=300+i)
                        i=i+30
                        displ.insert(END,detail)
        # func to exit
        def logout():
                exit(0)
        
        button1=Button(Home,text="exit",command=logout)
        button1.place(x=100,y=550)

        # user='wer'
        # passw='wer'
        super_part()
        student_dt()
        Home.mainloop()