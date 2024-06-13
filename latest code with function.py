from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def create_back_button(frame, command):
    BackImg = ImageTk.PhotoImage(Image.open(r"Back_Button(3).png").resize((30, 30)))
    back_button = Button(frame, image=BackImg, command=command, borderwidth=0)
    back_button.image = BackImg
    back_button.place(x=10, y=10)

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
    frame.pack(fill=BOTH, expand=True)

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

    snacks_button = Button(frame, image=SnacksImg, command=snacks_page, bd=0, highlightthickness=0, bg="black")
    snacks_button.place(x=width / 1.8, y=height / 2.1, anchor=SE)

    drinks_button = Button(frame, image=DrinksImg, command=drinks_page, bd=0, highlightthickness=0, bg="black")
    drinks_button.place(x=width / 2.2, y=height / 1.9, anchor=NW)

    next_tab_button = Button(frame, image=MenuTabImg, bd=0, highlightthickness=0, bg="black")
    next_tab_button.place(x=width / 5.2, y=height / 1.05, anchor=SW)

    cart_tab_button = Button(frame, image=CartTabImg, bd=0, highlightthickness=0, bg="black")
    cart_tab_button.place(x=width - 100, y=height - 35, anchor=SE)
    root.mainloop()

def snacks_page():
    snacks_window = Toplevel(root)
    snacks_window.title("FFO")
    snacks_window.geometry("400x715")
    snacks_window.resizable(False,False)
    width = 400
    height = 715

    background_image = (Image.open(r"Window_Bg_Snacks(3).png").resize((400,715)))
    background_image = ImageTk.PhotoImage(background_image)
    BurgerImg= ImageTk.PhotoImage(Image.open(r"Burger_Button(3).png").resize((170,170)))
    FriesImg=ImageTk.PhotoImage(Image.open(r"Fries_Button(3).png").resize((170,170)))
    ShawarmaImg=ImageTk.PhotoImage(Image.open(r"Shawarma_Button(3).png").resize((170,170)))
    PizzaImg=ImageTk.PhotoImage(Image.open(r"Pizza_Button(3).png").resize((170,170)))
    SiomaImg=ImageTk.PhotoImage(Image.open(r"Siomai_Button(3).png").resize((170,170)))
    BackImg=ImageTk.PhotoImage(Image.open(r"Back_Button(3).png").resize((30,30)))

    frame = Frame(snacks_window)
    frame.pack(fill=BOTH, expand=True)

    # Canvas Image
    canvas1 = Canvas(frame, bg="white", height=height, width=width, highlightthickness=0)
    canvas1.create_image(0, 0, anchor=NW, image=background_image)
    canvas1.pack(padx=0.1,pady=0.1)

    # Create Buttons
    burger_button = Button(frame, image=BurgerImg, command=on_burger_click, borderwidth=0)
    burger_button.place(x=15, y=110)

    fries_button = Button(frame, image=FriesImg, command=on_fries_click, borderwidth=0)
    fries_button.place(x=215, y=110)

    shawarma_button = Button(frame, image=ShawarmaImg, command=on_shawarma_click, borderwidth=0)
    shawarma_button.place(x=15, y=300)

    pizza_button = Button(frame, image=PizzaImg, command=on_pizza_click, borderwidth=0)
    pizza_button.place(x=215, y=300)

    siomai_button = Button(frame, image=SiomaImg, command=on_siomai_click, borderwidth=0)
    siomai_button.place(x=115, y=500)

    back_button = Button(frame, image=BackImg, command=snacks_window.destroy, borderwidth=0)
    back_button.place(x=10, y=10)
    root.mainloop()

def on_burger_click():
    messagebox.showinfo("Info", "Burger Button Clicked")

def on_fries_click():
    messagebox.showinfo("Info", "Fries Button Clicked")

def on_shawarma_click():
    messagebox.showinfo("Info", "Shawarma Button Clicked")

def on_pizza_click():
    messagebox.showinfo("Info", "Pizza Button Clicked")

def on_siomai_click():
    messagebox.showinfo("Info", "Siomai Button Clicked")

def drinks_page():
    drinks_window = Toplevel(root)
    drinks_window.title("FFO")
    drinks_window.geometry("400x715")
    drinks_window.resizable(False,False)
    width = 400
    height = 715

    # ICON IMAGE
    background_image = (Image.open(r"Window_Bg_Drinks(3).png").resize((400,715)))
    background_image = ImageTk.PhotoImage(background_image)
    CokeImg = ImageTk.PhotoImage(Image.open(r"Coke_Button(3).png").resize((170,170)))
    SpriteImg = ImageTk.PhotoImage(Image.open(r"Sprite_Button(3).png").resize((170,170)))
    CokeFloatImg = ImageTk.PhotoImage(Image.open(r"CokeFloat_Button(3).png").resize((170,170)))
    IcedTeaImg = ImageTk.PhotoImage(Image.open(r"IcedTea_Button(3).png").resize((170,170)))
    PineappleJuiceImg = ImageTk.PhotoImage(Image.open(r"PineappleJuice_Button(3).png").resize((170,170)))
    BackImg = ImageTk.PhotoImage(Image.open(r"Back_Button(3).png").resize((30,30)))

    frame = Frame(drinks_window)
    frame.pack(fill=BOTH, expand=True)  # Use BOTH and expand=True to make the frame expand

    # Canvas Image
    canvas1 = Canvas(frame, bg="white", height=height, width=width, highlightthickness=0)
    canvas1.create_image(0, 0, anchor=NW, image=background_image)
    canvas1.pack(padx=0.1, pady=0.1)

    # Create Buttons
    coke_button = Button(frame, image=CokeImg, command=on_coke_click, borderwidth=0)
    coke_button.place(x=15, y=110)

    sprite_button = Button(frame, image=SpriteImg, command=on_sprite_click, borderwidth=0)
    sprite_button.place(x=215, y=110)

    cokefloat_button = Button(frame, image=CokeFloatImg, command=on_cokefloat_click, borderwidth=0)
    cokefloat_button.place(x=15, y=300)

    icedtea_button = Button(frame, image=IcedTeaImg, command=on_icedtea_click, borderwidth=0)
    icedtea_button.place(x=215, y=300)

    pineapplejuice_button = Button(frame, image=PineappleJuiceImg, command=on_pineapplejuice_click, borderwidth=0)
    pineapplejuice_button.place(x=115, y=500)

    back_button = Button(frame, image=BackImg, command=drinks_window.destroy, borderwidth=0)
    back_button.place(x=10, y=10)

    root.mainloop()

def on_coke_click():
    messagebox.showinfo("Info", "Coke Button Clicked")

def on_sprite_click():
    messagebox.showinfo("Info", "Sprite Button Clicked")

def on_cokefloat_click():
    messagebox.showinfo("Info", "Coke Float Button Clicked")

def on_icedtea_click():
    messagebox.showinfo("Info", "Iced Tea Button Clicked")

def on_pineapplejuice_click():
    messagebox.showinfo("Info", "Pineapple Juice Button Clicked")

first_page()
