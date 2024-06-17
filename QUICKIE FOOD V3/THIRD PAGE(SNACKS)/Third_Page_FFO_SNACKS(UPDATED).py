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
        self.background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\THIRD PAGE(SNACKS)\ThirdWinBg(SNACKS).png"))
        self.burger_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\THIRD PAGE(SNACKS)\BurgerICON.png").resize((170, 170)))
        self.fries_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\THIRD PAGE(SNACKS)\FriesICON.png").resize((170, 170)))
        self.shawarma_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\THIRD PAGE(SNACKS)\ShawarmaICON.png").resize((170, 170)))
        self.pizza_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\THIRD PAGE(SNACKS)\PizzaICON.png").resize((170, 170)))
        self.siomai_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\THIRD PAGE(SNACKS)\SiomaiICON.png").resize((170, 170)))
        self.back_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\THIRD PAGE(SNACKS)\BackICON.png").resize((30, 30)))

    def create_frame(self):
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=True)

    def create_canvas(self):
        width = 400
        height = 715

        self.canvas1 = Canvas(self.frame, bg="white", height=height, width=width, highlightthickness=0)
        self.canvas1.create_image(0, 0, anchor=NW, image=self.background_image)
        self.canvas1.create_image(width / 2.1, height / 2.3, anchor=SE, image=self.burger_img)
        self.canvas1.create_image(width / 1.055, height / 2.275, anchor=SE, image=self.fries_img)
        self.canvas1.create_image(width / 2.1, height / 2.3, anchor=NE, image=self.shawarma_img)
        self.canvas1.create_image(width / 1.055, height / 2.275, anchor=NE, image=self.pizza_img)
        self.canvas1.create_image(width / 1.4, height / 1.115, anchor=SE, image=self.siomai_img)
        self.canvas1.create_image(width / 11, height / 14, anchor=SE, image=self.back_img)
        self.canvas1.pack(padx=0.1, pady=0.1)

def main():
    root = CTk()
    app = FFOApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()