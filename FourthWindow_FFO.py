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
root.geometry("400X217")
root.resizable(False,False)
width = 400
height = 217

# ICON IMAGE
background_image = Image.open(r"C:\Users\Admin\Downloads\Window_Bg(4)UPDATEEEED.png")
background_image = ImageTk.PhotoImage(background_image)
BackImg=ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\Back_Button(3).png").resize((20,20)))
ConfirmImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Pictures\Confirm_button(5).png").resize((200,50)))
AddImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Pictures\Add_Button(4).png").resize((30,30)))
MinusImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Pictures\Minus_Button(4).png").resize((30,30)))

frame = Frame(root)
frame.pack(fill=BOTH, expand=True)  # Use BOTH and expand=True to make the frame expand


#Labels mababago dipende sa user
Food = customtkinter.CTkLabel(master=root, text="Burger", width=25, height=25, fg_color="transparent", text_color="white", font=("Montserrat", 35), corner_radius=0)
Food.place(relx=0.1,rely=0.2)  
Price = customtkinter.CTkLabel(master=root, text="$1.99", width=25, height=25, fg_color="transparent", text_color="white", font=("Canva Sans", 32), corner_radius=0)
Price.place(relx=0.1, rely= 0.38)
Quantity= customtkinter.CTkLabel(master=root, text="1", width=25, height=25, fg_color="#ffffff", text_color="black", font=("Montserrat", 28), corner_radius=0)
Quantity.place(relx=0.68,rely=0.53) 

# Canvas Image
canvas1 = Canvas(frame, bg="white", height=height, width=width, highlightthickness=0)
canvas1.create_image(0, 0, anchor=NW, image=background_image)
canvas1_image = background_image
canvas1.create_image(width/15, height/10, anchor=SE, image=BackImg)
canvas1.create_image(width/2.1, height/1.25, anchor=N, image=ConfirmImg)
canvas1.create_image(width/1.155, height/1.85, anchor=NW, image=AddImg)
canvas1.create_image(width/2, height/1.85, anchor=NW, image=MinusImg)
canvas1.pack(padx=0, pady=0)



root.mainloop()