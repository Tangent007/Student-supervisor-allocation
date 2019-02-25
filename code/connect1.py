import tkinter as tk


def fun():
    root = tk.Tk()
    img=tk.PhotoImage(file="F:\wowowowo\py project\Group 72.png")
    label=tk.Label(root,image=img)
    label.pack()
    root.mainloop()