from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
import csv


#window
root = Tk()
root.title("FFO")
root.geometry("400x724")
#root.iconbitmap("PNCLogo.ico")
image_0=Image.open(r"C:\Users\Admin\Downloads\QF_FirstWinBg.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0, column=0)
root.resizable(False,False)

#Creating a photoimage object to use image 
photo1 = PhotoImage(file = r"C:\Users\Admin\Downloads\QF_FirstWinButton1.png") 
photo2 = PhotoImage(file = r"C:\Users\Admin\Downloads\QF_FirstWinButton2.png")
  
#Resizing image to fit on button 
photoimage = photo1.subsample(3,3) 
photoimage = photo2.subsample(3,3)
  
#Button1
DineInButton=Button(root, text =" " , image = photo1).place(relx = 0.2, rely = 0.2) 

#Button2
TakeOutButton=Button(root, text =" " , image = photo2).place(relx = 0.2, rely = 0.48) 




root.mainloop()