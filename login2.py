import tkinter as tk
import sqlite3
import tkinter.messagebox


logd=sqlite3.connect("stud_details.db")
logon=logd.cursor()


# import test2
# import signup_stu as s
root=tk.Tk()
var=tk.StringVar(root)

root.title("login_student")
root.geometry("1366x768")
image=tk.PhotoImage(file="F:\wowowowo\py project\home.png")
imagelabel=tk.Label(root,image=image,borderwidth=0)
imagelabel.pack(fill="both")

# func of login

# def log():
#     name = str(userl.get())
#     return name

def use():
    name1=userl.get()
    passw=pass1.get()
    # disp=tk.Text(master=root,height=10,width=30)
    # disp.place(x=30,y=30)
    # disp.insert(tk.END,name1)
    logon.execute("select * from login_details where Name=? and password=?",(name1,passw,))
    # for x in d:
    #     print(x)
    # if d.fetchone() is not None:
    #     print("Welcome")
    # else:
    #     print("Login failed")
    # # print(name1)
    d=logon.fetchone()
    if d is not None:
        print(d)
    else:
        # print('Login failed')
        tkinter.messagebox.showwarning("False Login" , "please try again")


# func of sign up

# def sign():
#     s.fun()
    

# user entry box

userl=tk.Entry()
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

pass1=tk.Entry(imagelabel,show="*",textvariable=var)
pass1.place(x=440,y=330)

# login label link

logo=tk.PhotoImage(file="F:\wowowowo\py project\Group 72.png")
logo1=tk.Button(root,image=logo,borderwidth=0,bg="#E8E8E8",command=use)
logo1.place(x=500,y=380)



# sign up label link
logo2=tk.PhotoImage(file="F:\wowowowo\py project\Group 82.png")
logo3=tk.Button(root,image=logo2,borderwidth=0,bg="#E8E8E8",activebackground="#E8E8E8")
logo3.place(x=430,y=624)


# def run():
#     s1.runn()


root.mainloop()