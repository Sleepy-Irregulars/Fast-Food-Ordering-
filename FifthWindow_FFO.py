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
root.geometry("380x715")
root.resizable(False,False)
width = 380
height = 715

# ICON IMAGE
background_image = Image.open(r"C:\Users\Admin\Downloads\Picture1 (2).png")
background_image = ImageTk.PhotoImage(background_image)
ConfirmImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Pictures\Confirm_button(5).png").resize((250,75)))
MenuTabImg= ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\tab for page 2.png").resize((60,40)))
CartTabImg= ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\Cart.png").resize((60,40)))

frame = Frame(root)
frame.pack(fill=BOTH, expand=True)  # Use BOTH and expand=True to make the frame expand

frame1 = customtkinter.CTkScrollableFrame(master=root, width=325, height=300, border_width=0, fg_color="black", border_color="Black")
frame1.place(relx=0.05, rely=0.21)

# Configure grid columns
frame1.grid_columnconfigure(0, weight=1)
frame1.grid_columnconfigure(1, weight=1)
frame1.grid_columnconfigure(2, weight=1)

# Labels
Food = customtkinter.CTkLabel(master=frame1, text="Food", width=25, height=25, fg_color="black", text_color="white", font=("Agrandir", 19), corner_radius=0)
Food.grid(row=1, column=0, padx=(10, 5), pady=5, sticky=W)  
Number = customtkinter.CTkLabel(master=frame1, text="No.", width=25, height=25, fg_color="black", text_color="white", font=("Agrandir", 19), corner_radius=0)
Number.grid(row=1, column=1, padx=(10, 5), pady=5, sticky=N+S+E+W)  
Price = customtkinter.CTkLabel(master=frame1, text="Price", width=25, height=25, fg_color="black", text_color="white", font=("Agrandir", 19), corner_radius=0)
Price.grid(row=1, column=2, padx=(10, 5), pady=5, sticky=W) 

Est= customtkinter.CTkLabel(master=root, text="10", width=25, height=25, fg_color="black", text_color="white", font=("Montserrat", 20), corner_radius=0)
Est.place(relx=0.2,rely=0.695)
Time= customtkinter.CTkLabel(master=root, text="mins", width=25, height=25, fg_color="black", text_color="white", font=("Montserrat", 20), corner_radius=0)
Time.place(relx=0.33,rely=0.695)
Total= customtkinter.CTkLabel(master=root, text="$4.00", width=25, height=25, fg_color="black", text_color="white", font=("Montserrat", 20), corner_radius=0)
Total.place(relx=0.75,rely=0.695)

# Orders
Order = customtkinter.CTkLabel(master=frame1, text="Burger", width=25, height=25, fg_color="black", text_color="white", font=("Agrandir", 19), corner_radius=0)
Order.grid(row=2, column=0, padx=(10, 5), pady=5, sticky=W)  
Num = customtkinter.CTkLabel(master=frame1, text="2", width=25, height=25, fg_color="black", text_color="white", font=("Agrandir", 19), corner_radius=0)
Num.grid(row=2, column=1, padx=(10, 5), pady=5, sticky=N+S+E+W)  
Cost = customtkinter.CTkLabel(master=frame1, text="$4.00", width=25, height=25, fg_color="black", text_color="white", font=("Agrandir", 19), corner_radius=0)
Cost.grid(row=2, column=2, padx=(10, 5), pady=5, sticky=W) 

# Canvas Image
canvas1 = Canvas(frame, bg="white", height=height, width=width, highlightthickness=0)
canvas1.create_image(185, 0, anchor=N, image=background_image)
canvas1_image = background_image
canvas1.create_image(width/2.1, height/1.25, anchor=N, image=ConfirmImg)
canvas1.create_image(width/5.2, height/1.05, anchor=SW, image=MenuTabImg)
canvas1.create_image(width/1.3, height/1.115, anchor=NE, image=CartTabImg)

canvas1.place(relx=0, rely=0)

root.mainloop()
