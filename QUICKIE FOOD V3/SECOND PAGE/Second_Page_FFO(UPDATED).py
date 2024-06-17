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
        self.background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\SECOND PAGE\SeconWinBg.png"))
        self.snacks_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\SECOND PAGE\SnacksICON.png").resize((200, 169)))
        self.drinks_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\SECOND PAGE\DrinksICON.png").resize((200, 169)))
        self.menu_tab_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\SECOND PAGE\MenuICON.png").resize((60, 40)))
        self.cart_tab_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\SECOND PAGE\CartICON.png").resize((60, 40)))

    def create_frame(self):
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=True)

    def create_canvas(self):
        width = 400
        height = 715

        self.canvas1 = Canvas(self.frame, bg="white", height=height, width=width, highlightthickness=0)
        self.canvas1.create_image(0, 0, anchor=NW, image=self.background_image)
        self.canvas1.create_image(width / 1.8, height / 2.3, anchor=SE, image=self.snacks_img)
        self.canvas1.create_image(width / 2.2, height / 2, anchor=NW, image=self.drinks_img)
        self.canvas1.create_image(width / 5.2, height / 1.05, anchor=SW, image=self.menu_tab_img)
        self.canvas1.create_image(width / 1.3, height / 1.115, anchor=NE, image=self.cart_tab_img)
        self.canvas1.pack(padx=0.1, pady=0.1)

def main():
    root = CTk()
    app = FFOApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()