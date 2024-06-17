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
        self.background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\FIRST PAGE\FirstWinBg.png"))
        self.dine_in_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\FIRST PAGE\DineInICON.png").resize((200, 169)))
        self.take_out_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\FIRST PAGE\TakeOut ICON.png").resize((200, 169)))

    def create_frame(self):
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=True)

    def create_canvas(self):
        width = 400
        height = 715

        self.canvas1 = Canvas(self.frame, bg="white", height=height, width=width, highlightthickness=0)
        self.canvas1.create_image(0, 0, anchor=NW, image=self.background_image)
        self.canvas1.create_image(width/2, height/2, anchor=S, image=self.dine_in_img)
        self.canvas1.create_image(width/2, height/2, anchor=N, image=self.take_out_img)
        self.canvas1.pack(padx=0.1, pady=0.1)

def main():
    root = CTk()
    app = FFOApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()