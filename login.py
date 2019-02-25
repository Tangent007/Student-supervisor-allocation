from tkinter import *
root=Tk()
root.title("loginu")
root.geometry("1366x768")
root.config(bg="#E8E8E8")

frame=Frame(width=1240,height=750,bg="#FFFFFF")
frame.pack(padx=30,pady=100)

# welcome image label

welcomeimage=PhotoImage(file="F:\wowowowo\py project\Group 2.png")
welcomelabel=Label(frame,image=welcomeimage,borderwidth=0,width=700)
welcomelabel.pack(side="right",fill="y")

# login user input part frame

entrylabel=Frame(frame,bg="#ffffff",borderwidth=0,width=500)
entrylabel.pack(side="left")

# login text label

loginlabel=Label(entrylabel,text="Login",bg="#ffffff",anchor="center",borderwidth=0,width=300)
loginlabel.config(font=("Segoe Script",25))
loginlabel.pack(side="left")

# user name label
userimage=PhotoImage(file="F:\wowowowo\py project\Group 4.png")
userlabel=Label(entrylabel,image=userimage,borderwidth=0,width=500)
userlabel.pack(side="top",pady='5')

# password label
passimage=PhotoImage(file="F:\wowowowo\py project\Group 5.png")
passlabel=Label(entrylabel,image=passimage,borderwidth=0,width=500)
passlabel.pack(side="top",pady='5')
#
mainloop()


