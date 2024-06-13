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
        self.create_labels()
        self.create_canvas()

    def setup_root(self):
        self.root.title("FFO")
        self.root.geometry("400x217")
        self.root.resizable(False, False)

    def load_images(self):
        self.background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\Window_Bg(4)UPDATEEEED.png"))
        self.back_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Downloads\Back_Button(3).png").resize((20, 20)))
        self.confirm_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Pictures\Icons ng FFO Window 4-5\Confirm_button(5).png").resize((200, 50)))
        self.add_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Pictures\Icons ng FFO Window 4-5\Add_Button(4).png").resize((30, 30)))
        self.minus_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Pictures\Icons ng FFO Window 4-5\Minus_Button(4).png").resize((30, 30)))

    def create_frame(self):
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=True)

    def create_labels(self):
        self.food_label = customtkinter.CTkLabel(master=self.root, text="Burger", width=25, height=25, fg_color="transparent", text_color="white", font=("Montserrat", 35), corner_radius=0)
        self.food_label.place(relx=0.1, rely=0.2)

        self.price_label = customtkinter.CTkLabel(master=self.root, text="$1.99", width=25, height=25, fg_color="transparent", text_color="white", font=("Canva Sans", 32), corner_radius=0)
        self.price_label.place(relx=0.1, rely=0.38)

        self.quantity_label = customtkinter.CTkLabel(master=self.root, text="1", width=25, height=25, fg_color="#ffffff", text_color="black", font=("Montserrat", 28), corner_radius=0)
        self.quantity_label.place(relx=0.68, rely=0.53)

    def create_canvas(self):
        width = 400
        height = 217

        self.canvas1 = Canvas(self.frame, bg="white", height=height, width=width, highlightthickness=0)
        self.canvas1.create_image(0, 0, anchor=NW, image=self.background_image)
        self.canvas1.create_image(width / 15, height / 10, anchor=SE, image=self.back_img)
        self.canvas1.create_image(width / 2.1, height / 1.25, anchor=N, image=self.confirm_img)
        self.canvas1.create_image(width / 1.155, height / 1.85, anchor=NW, image=self.add_img)
        self.canvas1.create_image(width / 2, height / 1.85, anchor=NW, image=self.minus_img)
        self.canvas1.pack(padx=0, pady=0)

def main():
    root = CTk()
    app = FFOApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()