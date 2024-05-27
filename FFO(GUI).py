from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from customtkinter import *
from PIL import Image, ImageTk
import customtkinter
import mysql.connector
import csv


#window
root = CTk(fg_color="white")
root.title("FFO")
root.geometry("400x724")
#root.iconbitmap("PNCLogo.ico")
image_0=Image.open(r"C:\Users\Admin\Downloads\QF_FirstWinBg.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0, column=0)
root.resizable(False,False)

#Define Image 
Dine_In_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\QF_FirstWinButton1.png").resize((200,120))) 
Take_Out_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\QF_FirstWinButton2.png").resize((200,120)))



#Button1
DineInButton= customtkinter.CTkButton(master=root, width=200,
                                 height=120,
                                 border_width=0,
                                 corner_radius= 40,
                                 text=" ",fg_color= "#fab9b9",
                                 hover = False,
                                 image= Dine_In_img)
DineInButton.place(relx=0.125, rely=0.2)

#Button2
TakeOutButton= customtkinter.CTkButton(master=root, width=200,
                                 height=120,
                                 border_width=0,
                                 corner_radius= 40,
                                 text=" ",fg_color= "#dfe3ff",
                                 hover= False,
                                 image= Take_Out_img)
TakeOutButton.place(relx=0.125, rely=0.45)




root.mainloop()