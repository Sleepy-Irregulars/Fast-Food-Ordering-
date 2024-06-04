from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import tkinter
import csv
import ctypes


def snacks_clicked():
    pass


def drinks_clicked():
    pass



root = Tk()
root.title("FFO")
root.geometry("400x715")
root.resizable(False, False)
width = 400
height = 715

# ICON IMAGE
background_image = Image.open(r"main.png")
background_image = ImageTk.PhotoImage(background_image)
SnacksImg = ImageTk.PhotoImage(Image.open(
    r"SNACKS.png").resize(
    (200, 169)))
DrinksImg = ImageTk.PhotoImage(Image.open(
    r"Drinks.png").resize(
    (200, 169)))
MenuTabImg = ImageTk.PhotoImage(Image.open(
    r"tab for page 2.png").resize(
    (60, 40)))
CartTabImg = ImageTk.PhotoImage(Image.open(
    r"Cart.png").resize(
    (60, 40)))

frame = Frame(root)
frame.pack(fill=BOTH, expand=True)  # Use BOTH and expand=True to make the frame expand

# Canvas Image
canvas1 = Canvas(frame, bg="white", height=height, width=width, highlightthickness=0)
canvas1.create_image(0, 0, anchor=NW, image=background_image)
canvas1_image = background_image
canvas1.create_image(width / 1.8, height / 2.1, anchor=SE, image=SnacksImg)
canvas1.create_image(width / 2.2, height / 1.9, anchor=NW, image=DrinksImg)
canvas1.create_image(width / 5.2, height / 1.05, anchor=SW, image=MenuTabImg)
canvas1.create_image(width / 1.3, height / 1.115, anchor=NE, image=CartTabImg)
canvas1.pack(padx=0.1, pady=0.1)

snacks_button = Button(frame, image=SnacksImg, command=snacks_clicked, bd=0, highlightthickness=0, bg="black")
snacks_button.place(x=width / 1.8, y=height / 2.1, anchor=SE)

drinks_button = Button(frame, image=DrinksImg, command=drinks_clicked, bd=0, highlightthickness=0, bg="black" )
drinks_button.place(x=width / 2.2, y=height / 1.9, anchor=NW)

next_tab_button = Button(frame, image=MenuTabImg, bd=0, highlightthickness=0,bg="black")
next_tab_button.place(x=width / 5.2, y=height / 1.05, anchor=SW)

cart_tab_button = Button(frame, image=CartTabImg, bd=0, highlightthickness=0, bg="black")
cart_tab_button.place(x=width - 100, y=height - 35, anchor=SE)

root.mainloop()