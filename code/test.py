# create a Tkinter button with an image and optional text
# note that Tkinter reads only GIF and PGM/PPM images
# for other image file types use the Python Image Library (PIL)
# replace the line photo1 = tk.PhotoImage(file="Press1.gif")
# with these three lines ...
#
# from PIL import Image, ImageTk
# image1 = Image.open("Press1.jpg")
# photo1 = ImageTk.PhotoImage(image1)
#
# tested with Python24     vegaseat     23dec2006
import tkinter as tk
button_flag = True
def click():
    """
    respond to the button click
    """
    global button_flag
    # toggle button colors as a test
    if button_flag:
        button1.config(bg="white")
        button_flag = False
    else:
        button1.config(bg="green")
        button_flag = True
root = tk.Tk()
# create a frame and pack it
frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP, fill=tk.X)
# pick a (small) image file you have in the working directory ...
photo1 = tk.PhotoImage(file="F:\wowowowo\py project\signup_super.png")
# create the image button, image is above (top) the optional text
button1 = tk.Button(frame1, compound=tk.TOP, width=155, height=55, image=photo1,
    text="optional text", bg='green', command=click)
button1.pack(side=tk.LEFT, padx=2, pady=2)
# save the button's image from garbage collection (needed?)
button1.image = photo1
# start the event loop
root.mainloop()