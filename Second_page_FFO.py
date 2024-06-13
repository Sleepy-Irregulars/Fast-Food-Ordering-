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
background_image = Image.open(r"C:\Users\Admin\Downloads\Second Page.png")
background_image = ImageTk.PhotoImage(background_image)
SnacksImg= ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\SNACKS (2).png").resize((200,169)))
DrinksImg=ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\Drinks (2).png").resize((200,169)))
MenuTabImg= ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\tab for page 2.png").resize((60,40)))
CartTabImg= ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\Cart.png").resize((60,40)))

frame = Frame(root)
frame.pack(fill=BOTH, expand=True)  # Use BOTH and expand=True to make the frame expand

#Canvas Image
canvas1 = Canvas(frame, bg="white", height=height, width=width, highlightthickness=0)
canvas1.create_image(0, 0, anchor=NW, image=background_image)
canvas1_image = background_image
canvas1.create_image(width/1.8, height/2.3, anchor=SE, image=SnacksImg)
canvas1.create_image(width/2.2, height/2, anchor=NW, image=DrinksImg)
canvas1.create_image(width/5.2, height/1.05, anchor=SW, image=MenuTabImg)
canvas1.create_image(width/1.3, height/1.115, anchor=NE, image=CartTabImg)
canvas1.pack(padx=0.1,pady=0.1)

root.mainloop()