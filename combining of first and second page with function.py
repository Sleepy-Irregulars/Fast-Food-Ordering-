from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def first_page():
    global root
    root = Tk()
    root.title("FFO")
    root.geometry("400x715")
    root.resizable(False, False)
    width = 400
    height = 715

    background_image = Image.open(r"main.png")
    background_image = ImageTk.PhotoImage(background_image)
    DineInImg = ImageTk.PhotoImage(Image.open(r"dine in.png").resize((200, 169)))
    TakeOutImg = ImageTk.PhotoImage(Image.open(r"take out.png").resize((200, 169)))

    frame = Frame(root)
    frame.pack(fill=BOTH, expand=False)

    canvas1 = Canvas(frame, bg="white", height=height, width=width, highlightthickness=0)
    canvas1.create_image(0, 0, anchor=NW, image=background_image)
    canvas1_image = background_image
    canvas1.create_image(width / 2, height / 2.1, anchor=S, image=DineInImg)
    canvas1.create_image(width / 2, height / 1.6, anchor=N, image=TakeOutImg)
    canvas1.pack(padx=0.1, pady=0.1)

    dine_in_button = Button(frame, image=DineInImg, command=second_page, bd=0, highlightthickness=0, bg="black")
    dine_in_button.place(x=width / 2, y=height / 2.1, anchor=S)

    take_out_button = Button(frame, image=TakeOutImg, command=second_page, bd=0, highlightthickness=0, bg="black")
    take_out_button.place(x=width / 2, y=height / 1.6, anchor=N)

    root.mainloop()

def second_page():
    second_window = Toplevel(root)
    second_window.title("FFO")
    second_window.geometry("400x715")
    second_window.resizable(False, False)
    width = 400
    height = 715

    background_image = Image.open(r"main.png")
    background_image = ImageTk.PhotoImage(background_image)
    SnacksImg = ImageTk.PhotoImage(Image.open(r"SNACKS.png").resize((200, 169)))
    DrinksImg = ImageTk.PhotoImage(Image.open(r"Drinks.png").resize((200, 169)))
    MenuTabImg = ImageTk.PhotoImage(Image.open(r"tab for page 2.png").resize((60, 40)))
    CartTabImg = ImageTk.PhotoImage(Image.open(r"Cart.png").resize((60, 40)))

    frame = Frame(second_window)
    frame.pack(fill=BOTH, expand=True)

    canvas1 = Canvas(frame, bg="white", height=height, width=width, highlightthickness=0)
    canvas1.create_image(0, 0, anchor=NW, image=background_image)
    canvas1_image = background_image
    canvas1.create_image(width / 1.8, height / 2.1, anchor=SE, image=SnacksImg)
    canvas1.create_image(width / 2.2, height / 1.9, anchor=NW, image=DrinksImg)
    canvas1.create_image(width / 5.2, height / 1.05, anchor=SW, image=MenuTabImg)
    canvas1.create_image(width / 1.3, height / 1.115, anchor=NE, image=CartTabImg)
    canvas1.pack(padx=0.1, pady=0.1)

    snacks_button = Button(frame, image=SnacksImg, command=second_window.destroy, bd=0, highlightthickness=0, bg="black")
    snacks_button.place(x=width / 1.8, y=height / 2.1, anchor=SE)

    drinks_button = Button(frame, image=DrinksImg, command=second_window.destroy, bd=0, highlightthickness=0, bg="black")
    drinks_button.place(x=width / 2.2, y=height / 1.9, anchor=NW)

    next_tab_button = Button(frame, image=MenuTabImg, bd=0, highlightthickness=0, bg="black")
    next_tab_button.place(x=width / 5.2, y=height / 1.05, anchor=SW)

    cart_tab_button = Button(frame, image=CartTabImg, bd=0, highlightthickness=0, bg="black")
    cart_tab_button.place(x=width - 100, y=height - 35, anchor=SE)
    root.mainloop()
first_page()
