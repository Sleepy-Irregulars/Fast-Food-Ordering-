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
        self.create_scrollable_frame()
        self.create_labels()
        self.create_canvas()
        self.create_order_labels()

    def setup_root(self):
        self.root.title("FFO")
        self.root.geometry("380x715")
        self.root.resizable(False, False)
        self.width = 380
        self.height = 715

    def load_images(self):
        self.background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\FIFTH PAGE\FifthWinBg.png"))
        self.confirm_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\FIFTH PAGE\ConfirmICON.png").resize((250, 75)))
        self.menu_tab_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\FIFTH PAGE\MenuICON.png").resize((60, 40)))
        self.cart_tab_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\QUICKIE FOOD V3\FIFTH PAGE\CartICON.png").resize((60, 40)))

    def create_frame(self):
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=True)

    def create_scrollable_frame(self):
        self.scrollable_frame = customtkinter.CTkScrollableFrame(master=self.root, width=325, height=300, border_width=0, fg_color="black", border_color="Black")
        self.scrollable_frame.place(relx=0.05, rely=0.21)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.scrollable_frame.grid_columnconfigure(2, weight=1)

    def create_labels(self):
        self.food_label = customtkinter.CTkLabel(master=self.scrollable_frame, text="Food", width=25, height=25, fg_color="black", text_color="white", font=("Agrandir", 19), corner_radius=0)
        self.food_label.grid(row=1, column=0, padx=(10, 5), pady=5, sticky=W)
        
        self.number_label = customtkinter.CTkLabel(master=self.scrollable_frame, text="No.", width=25, height=25, fg_color="black", text_color="white", font=("Agrandir", 19), corner_radius=0)
        self.number_label.grid(row=1, column=1, padx=(10, 5), pady=5, sticky=N+S+E+W)
        
        self.price_label = customtkinter.CTkLabel(master=self.scrollable_frame, text="Price", width=25, height=25, fg_color="black", text_color="white", font=("Agrandir", 19), corner_radius=0)
        self.price_label.grid(row=1, column=2, padx=(10, 5), pady=5, sticky=W)

        self.est_label = customtkinter.CTkLabel(master=self.root, text="10", width=25, height=25, fg_color="black", text_color="white", font=("Montserrat", 20), corner_radius=0)
        self.est_label.place(relx=0.2, rely=0.695)
        
        self.time_label = customtkinter.CTkLabel(master=self.root, text="mins", width=25, height=25, fg_color="black", text_color="white", font=("Montserrat", 20), corner_radius=0)
        self.time_label.place(relx=0.33, rely=0.695)
        
        self.total_label = customtkinter.CTkLabel(master=self.root, text="$4.00", width=25, height=25, fg_color="black", text_color="white", font=("Montserrat", 20), corner_radius=0)
        self.total_label.place(relx=0.75, rely=0.695)

    def create_canvas(self):
        self.canvas1 = Canvas(self.frame, bg="white", height=self.height, width=self.width, highlightthickness=0)
        self.canvas1.create_image(185, 0, anchor=N, image=self.background_image)
        self.canvas1.create_image(self.width / 2.1, self.height / 1.25, anchor=N, image=self.confirm_img)
        self.canvas1.create_image(self.width / 5.2, self.height / 1.05, anchor=SW, image=self.menu_tab_img)
        self.canvas1.create_image(self.width / 1.3, self.height / 1.115, anchor=NE, image=self.cart_tab_img)
        self.canvas1.place(relx=0, rely=0)

    def create_order_labels(self):
        order = customtkinter.CTkLabel(master=self.scrollable_frame, text="Burger", width=25, height=25, fg_color="black", text_color="white", font=("Agrandir", 19), corner_radius=0)
        order.grid(row=2, column=0, padx=(10, 5), pady=5, sticky=W)
        
        num = customtkinter.CTkLabel(master=self.scrollable_frame, text="2", width=25, height=25, fg_color="black", text_color="white", font=("Agrandir", 19), corner_radius=0)
        num.grid(row=2, column=1, padx=(10, 5), pady=5, sticky=N+S+E+W)
        
        cost = customtkinter.CTkLabel(master=self.scrollable_frame, text="$4.00", width=25, height=25, fg_color="black", text_color="white", font=("Agrandir", 19), corner_radius=0)
        cost.grid(row=2, column=2, padx=(10, 5), pady=5, sticky=W)

def main():
    root = CTk()
    app = FFOApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()