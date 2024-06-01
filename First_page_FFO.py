from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from customtkinter import *
from PIL import Image, ImageTk
import customtkinter
import mysql.connector
import csv
import ctypes

root = CTk()
root.title("FFO")
root.geometry("400x715")
root.resizable(False,False)
width = 400
height = 715

# ICON IMAGE
background_image = Image.open(r"C:\Users\Admin\Desktop\FFO OOP\FirstWin_Bg.png")
background_image = ImageTk.PhotoImage(background_image)
DineInImg= ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\Dine In.png").resize((200,169)))
TakeOutImg=ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\FFO OOP\Take Out.png").resize((200,169)))

frame = Frame(root)
frame.pack(fill=BOTH, expand=True)  # Use BOTH and expand=True to make the frame expand

#Canvas Image
canvas1 = Canvas(frame, bg="white", height=height, width=width, highlightthickness=0)
canvas1.create_image(0, 0, anchor=NW, image=background_image)
canvas1_image = background_image
canvas1.create_image(width/2, height/2, anchor=S, image=DineInImg)
canvas1.create_image(width/2, height/2, anchor=N, image=TakeOutImg)
canvas1.pack(padx=0.1,pady=0.1)

root.mainloop()
