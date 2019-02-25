import tkinter as tk
# import test2
import signup_stu as s
root=tk.Tk()

root.title("login_student")
root.geometry("1366x768")
image=tk.PhotoImage(file="F:\wowowowo\py project\home.png")
imagelabel=tk.Label(root,image=image,borderwidth=0)
imagelabel.pack(fill="both")

# func of login

def log():
    name = str(userl.get())
    return name

def use():
    name1=log()
    disp=tk.Text(master=root,height=10,width=30)
    disp.place(x=30,y=30)
    disp.insert(tk.END,name1)
    # print(name1)

# func of sign up

def sign():
    s.fun()
    

# user entry box

userl=tk.Entry()
# userl.config(width=20,height=20)
userl.place(x=440,y=280)
# print(userl.get())

# password entry box

pass1=tk.Entry(show="*")
pass1.place(x=440,y=330)

# login label link

logo=tk.PhotoImage(file="F:\wowowowo\py project\Group 72.png")
logo1=tk.Button(root,image=logo,borderwidth=0,bg="#E8E8E8",command=use)
logo1.place(x=500,y=380)



# sign up label link
logo2=tk.PhotoImage(file="F:\wowowowo\py project\Group 82.png")
logo3=tk.Button(root,image=logo2,borderwidth=0,bg="#E8E8E8",activebackground="#E8E8E8",command=sign)
logo3.place(x=430,y=624)


# def run():
#     s1.runn()


root.mainloop()