import cv2
from tkinter import *
from tkinter import tix
from tkinter import filedialog
from PIL import Image, imageTk


tk = Tk

tk.wn_title("HDetector v0.1")
tk.geometry('1280*800')
tk.config(background = "#FFFFFF" )

tk.resizable(0.0)
imageFrame = Tik.Frame(tk, width=1280, height =800)
imageFrame.grid(row=0, column=0, padx=2, pady=2)

lmain = ttk.Label(imageFrame)
Imain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    img = Image.fromarrat(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)

    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)


def open_file():

    filepath = filedialog.ascopenfilename()

    if filepath !="":
        print(filepath)
        return filepath
    else:
        return None

def close():
    tk.destroy()
    tk.quit()


open_button = Button(imageFrame, text = "Open file", command = open_file)
open_button.grid(row=100, column=0, sticky=NSEW, padx=2, pady=2)
tk.protocol('WM_DELETE_WINDOW', close)


show_frame()
tk.mainloop()