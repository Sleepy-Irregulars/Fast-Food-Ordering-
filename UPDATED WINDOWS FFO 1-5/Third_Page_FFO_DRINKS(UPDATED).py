from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from customtkinter import *
from PIL import Image, ImageTk
import customtkinter
import mysql.connector
import csv
import ctypes

class FFOApp:
    def __init__(self, root):
        self.root = root
        self.setup_root()
        self.load_images()
        self.create_frame()
        self.create_canvas()

    def setup_root(self):
        self.root.title("FFO")
        self.root.geometry("400x715")
        self.root.resizable(False, False)

    def load_images(self):
        self.background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\Window_Bg_Drinks(3).png"))
        self.coke_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\Coke_Button(3).png").resize((170, 170)))
        self.sprite_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Pictures\Icons ng FFO Window 4-5\Sprite_Button(3)UPDATED.png").resize((170, 170)))
        self.cokefloat_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Pictures\Icons ng FFO Window 4-5\CokeFloat_Butto(3)UPDATED.png").resize((170, 170)))
        self.icedtea_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\IcedTea_Button(3).png").resize((170, 170)))
        self.pineapplejuice_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\PineappleJuice_Button(3).png").resize((170, 170)))
        self.back_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\Back_Button(3).png").resize((30, 30)))

    def create_frame(self):
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=True)

    def create_canvas(self):
        width = 400
        height = 715

        self.canvas1 = Canvas(self.frame, bg="white", height=height, width=width, highlightthickness=0)
        self.canvas1.create_image(0, 0, anchor=NW, image=self.background_image)
        self.canvas1.create_image(width / 2.1, height / 2.3, anchor=SE, image=self.coke_img)
        self.canvas1.create_image(width / 1.055, height / 2.275, anchor=SE, image=self.sprite_img)
        self.canvas1.create_image(width / 2.1, height / 2.3, anchor=NE, image=self.cokefloat_img)
        self.canvas1.create_image(width / 1.055, height / 2.275, anchor=NE, image=self.icedtea_img)
        self.canvas1.create_image(width / 1.4, height / 1.115, anchor=SE, image=self.pineapplejuice_img)
        self.canvas1.create_image(width / 11, height / 14, anchor=SE, image=self.back_img)
        self.canvas1.pack(padx=0.1, pady=0.1)

def main():
    root = CTk()
    app = FFOApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()