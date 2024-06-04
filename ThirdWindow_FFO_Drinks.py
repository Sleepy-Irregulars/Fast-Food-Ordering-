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
background_image = Image.open(r"C:\Users\User\Downloads\FFO\Window_Bg_Snacks(3).png")
background_image = ImageTk.PhotoImage(background_image)
CokeImg= ImageTk.PhotoImage(Image.open(r"C:\Users\User\Downloads\FFO\Coke_Button(3).png").resize((170,170)))
SpriteImg=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Downloads\FFO\Sprite_Button(3).png").resize((170,170)))
CokeFloatImg=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Downloads\FFO\CokeFloat_Button(3).png").resize((170,170)))
IcedTeaImg=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Downloads\FFO\IcedTea_Button(3).png").resize((170,170)))
PineappleJuiceImg=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Downloads\FFO\PineappleJuice_Button(3).png").resize((170,170)))
BackImg=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Downloads\FFO\Back_Button(3).png").resize((30,30)))

frame = Frame(root)
frame.pack(fill=BOTH, expand=True)  # Use BOTH and expand=True to make the frame expand

#Canvas Image
canvas1 = Canvas(frame, bg="white", height=height, width=width, highlightthickness=0)
canvas1.create_image(0, 0, anchor=NW, image=background_image)
canvas1_image = background_image
canvas1.create_image(width/2.1, height/2.3, anchor=SE, image=CokeImg)
canvas1.create_image(width/1.055, height/2.275, anchor=SE, image=SpriteImg)
canvas1.create_image(width/2.1, height/2.3, anchor=NE, image=CokeFloatImg)
canvas1.create_image(width/1.055, height/2.275, anchor=NE, image=IcedTeaImg)
canvas1.create_image(width/1.4, height/1.115, anchor=SE, image=PineappleJuiceImg)
canvas1.create_image(width/11, height/14, anchor=SE, image=BackImg)
canvas1.pack(padx=0.1,pady=0.1)

root.mainloop()