from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter
from customtkinter import*

root= CTk(fg_color="black")
root.title("FFO")
root.geometry("400x715")
image_0=Image.open(r"C:\Users\User\Downloads\FFO\FirstWin_Bg.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0,column=0)
root.resizable(False,False)


root.mainloop()