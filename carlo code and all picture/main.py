import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# Global cart list to store ordered items
cart = []

def create_back_button(frame, command):
    BackImg = ImageTk.PhotoImage(Image.open(r"back button.png").resize((30, 30)))
    back_button = Button(frame, image=BackImg, command=command, borderwidth=0)
    back_button.image = BackImg
    back_button.place(x=10, y=10)

def initialize_database():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('ffo_cart.db')
    cursor = conn.cursor()
    # Create the cart table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS cart
                      (id INTEGER PRIMARY KEY, food TEXT, quantity INTEGER, price REAL)''')
    conn.commit()
    conn.close()

def add_to_cart(food, quantity, price):
    conn = sqlite3.connect('ffo_cart.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO cart (food, quantity, price) VALUES (?, ?, ?)''', (food, quantity, price))
    conn.commit()
    conn.close()

def get_cart_items():
    conn = sqlite3.connect('ffo_cart.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT food, quantity, price FROM cart''')
    items = cursor.fetchall()
    conn.close()
    return items

def clear_cart():
    conn = sqlite3.connect('ffo_cart.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM cart''')
    conn.commit()
    conn.close()

def first_page():
    global root
    root = Tk()
    root.title("FFO")
    root.geometry("400x715")
    root.resizable(False, False)
    width = 400
    height = 715

    background_image = (Image.open(r"main.png").resize((400, 715)))
    background_image = ImageTk.PhotoImage(background_image)
    DineInImg = ImageTk.PhotoImage(Image.open(r"ain.png").resize((340, 189)))
    TakeOutImg = ImageTk.PhotoImage(Image.open(r"a.png").resize((340, 189)))

    frame = Frame(root)
    frame.pack(fill=BOTH, expand=False)

    canvas1 = Canvas(frame, height=height, width=width, highlightthickness=0)
    canvas1.create_image(0, 0, anchor=NW, image=background_image)
    canvas1_image = background_image
    canvas1.create_image(width / 2, height / 2.1, anchor=S, image=DineInImg)
    canvas1.create_image(width / 2, height / 1.8, anchor=N, image=TakeOutImg)
    canvas1.pack(padx=0.1, pady=0.1)

    dine_in_button = Button(frame, image=DineInImg, command=lambda: open_new_window(root, second_page), bd=0, highlightthickness=0)
    dine_in_button.place(x=width / 2, y=height / 2.1, anchor=S)

    take_out_button = Button(frame, image=TakeOutImg,  command=lambda: open_new_window(root, second_page), bd=0, highlightthickness=0)
    take_out_button.place(x=width / 2, y=height / 1.8, anchor=N)

    root.mainloop()


def open_new_window(current_window, new_window_func):
    current_window.destroy()
    new_window_func()






def second_page():
    second_window = Tk()
    second_window.title("FFO")
    second_window.geometry("400x715")
    second_window.resizable(False, False)
    width = 400
    height = 715

    background_image = Image.open(r"Second Page (1).png").resize((400, 715))
    background_image = ImageTk.PhotoImage(background_image)
    SnacksImg = ImageTk.PhotoImage(Image.open(r"nacks.png").resize((200, 169)))
    DrinksImg = ImageTk.PhotoImage(Image.open(r"rinks.png").resize((200, 169)))
    MenuTabImg = ImageTk.PhotoImage(Image.open(r"tab.png").resize((60, 40)))
    CartTabImg = ImageTk.PhotoImage(Image.open(r"buttoncart.png").resize((60, 40)))

    frame = Frame(second_window)
    frame.pack(fill=BOTH, expand=True)

    canvas1 = Canvas(frame, height=height, width=width, highlightthickness=0)
    canvas1.create_image(0, 0, anchor=NW, image=background_image)
    canvas1_image = background_image
    canvas1.create_image(width / 1.8, height / 2.1, anchor=SE, image=SnacksImg)
    canvas1.create_image(width / 2.2, height / 1.9, anchor=NW, image=DrinksImg)
    canvas1.create_image(width / 5.2, height / 1.05, anchor=SW, image=MenuTabImg)
    canvas1.create_image(width / 1.3, height / 1.115, anchor=NE, image=CartTabImg)
    canvas1.pack(padx=0.1, pady=0.1)

    snacks_button = Button(frame, image=SnacksImg, command=lambda: open_new_window(second_window, snacks_page), bd=0, highlightthickness=0)
    snacks_button.place(x=width / 1.8, y=height / 2.1, anchor=SE)

    drinks_button = Button(frame, image=DrinksImg, command=lambda: open_new_window(second_window, drinks_page), bd=0, highlightthickness=0)
    drinks_button.place(x=width / 2.2, y=height / 1.9, anchor=NW)

    next_tab_button = Button(frame, image=MenuTabImg, command=lambda: open_new_window(second_window, first_page), bd=0, highlightthickness=0, bg="black")
    next_tab_button.place(x=width / 5.2, y=height / 1.05, anchor=SW)

    cart_tab_button = Button(frame, image=CartTabImg, bd=0, highlightthickness=0, bg="black", command=lambda: open_new_window(second_window, view_cart))
    cart_tab_button.place(x=width - 90, y=height - 35, anchor=SE)

    second_window.mainloop()

def view_cart():
    cart_window = Tk()
    cart_window.title("Your Cart")
    cart_window.geometry("400x715")
    cart_window.resizable(False, False)
    width = 400
    height = 715

    background_image = Image.open(r"windowcart.png").resize((400, 715))
    placeorderTabImg = ImageTk.PhotoImage(Image.open(r"confirm.png").resize((210, 50)))
    BackImg = ImageTk.PhotoImage(Image.open(r"back button.png").resize((30, 30)))
    MenuTabImg = ImageTk.PhotoImage(Image.open(r"tab.png").resize((60, 40)))
    CartTabImg = ImageTk.PhotoImage(Image.open(r"buttoncart.png").resize((60, 40)))
    background_image = ImageTk.PhotoImage(background_image)

    frame = Frame(cart_window)
    frame.pack(fill=BOTH, expand=True)

    canvas1 = Canvas(frame, height=height, width=width, highlightthickness=0)
    canvas1.create_image(0, 0, anchor=NW, image=background_image)
    canvas1.pack(padx=0.1, pady=0.1)

    # Create a frame for the cart details
    details_frame = Frame(cart_window, bg="white")
    details_frame.place(x=8, y=150, width=380, height=330)

    # Add headers
    headers = ["Food", "No.", "Price"]
    for i, header in enumerate(headers):
        header_label = Label(details_frame, text=header, font=("Helvetica", 12, "bold"), bg="white")
        header_label.grid(row=0, column=i, padx=45, pady=10)

    # Retrieve cart items from database
    cart_items = get_cart_items()

    # Add cart items to the frame
    for i, item in enumerate(cart_items, start=1):
        Label(details_frame, text=item[0], font=("Helvetica", 12), bg="white").grid(row=i, column=0, padx=10, pady=5)
        Label(details_frame, text=item[1], font=("Helvetica", 12), bg="white").grid(row=i, column=1, padx=10, pady=5)
        Label(details_frame, text=f"₱{item[2]:.2f}", font=("Helvetica", 12), bg="white").grid(row=i, column=2, padx=10, pady=5)

    # Calculate total
    total = sum(item[1] * item[2] for item in cart_items)
    estimated_time = 20

    # Add EST and Total
    est_label = Label(cart_window, text=f" {estimated_time} min", font=("Helvetica", 14), relief=SUNKEN, bg="white")
    est_label.place(x=80, y=510)

    total_label = Label(cart_window, text=f" ₱{total:.2f}", font=("Helvetica", 14), relief=SUNKEN, bg="white")
    total_label.place(x=290, y=510)

    # Confirm button
    confirm_button = Button(cart_window, image=placeorderTabImg, bd=0, highlightthickness=0, command=confirm_order)
    confirm_button.place(x=width - 210, y=height - 99, anchor=CENTER)

    next_tab_button = Button(frame, image=MenuTabImg, command=lambda: open_new_window(cart_window, first_page), bd=0,
                             highlightthickness=0, bg="black")
    next_tab_button.place(x=width / 4.6, y=height / 1.03, anchor=SW)

    cart_tab_button = Button(frame, image=CartTabImg, bd=0, highlightthickness=0, bg="black",
                             command=lambda: open_new_window(cart_window, view_cart))
    cart_tab_button.place(x=width - 86, y=height  / 1.03, anchor=SE)

    back_button = Button(frame, image=BackImg, command=lambda: open_new_window(cart_window, second_page),
                         borderwidth=0, highlightthickness=0)
    back_button.place(x=10, y=10)

    cart_window.mainloop()

def confirm_order():
    clear_cart()
    messagebox.showinfo("Order Confirmed", "You have successfully placed your order!")

def snacks_page():
    snacks_window = Tk()
    snacks_window.title("FFO")
    snacks_window.geometry("400x715")
    snacks_window.resizable(False, False)
    width = 400
    height = 715

    background_image = (Image.open(r"Window_Bg_Snacks(3).png").resize((400, 715)))
    background_image = ImageTk.PhotoImage(background_image)
    BurgerImg = ImageTk.PhotoImage(Image.open(r"burger.png").resize((170, 170)))
    FriesImg = ImageTk.PhotoImage(Image.open(r"fries.png").resize((170, 170)))
    ShawarmaImg = ImageTk.PhotoImage(Image.open(r"shawarma.png").resize((170, 170)))
    PizzaImg = ImageTk.PhotoImage(Image.open(r"pizza.png").resize((170, 170)))
    SiomaImg = ImageTk.PhotoImage(Image.open(r"siomai.png").resize((170, 170)))
    BackImg = ImageTk.PhotoImage(Image.open(r"back button.png").resize((30, 30)))

    frame = Frame(snacks_window)
    frame.pack(fill=BOTH, expand=True)

    # Canvas Image
    canvas1 = Canvas(frame, height=height, width=width, highlightthickness=0)
    canvas1.create_image(0, 0, anchor=NW, image=background_image)
    canvas1.pack(padx=0.1, pady=0.1)

    # Create Buttons
    burger_button = Button(frame, image=BurgerImg,  command=lambda: open_new_window(snacks_window, burger_window), borderwidth=0, highlightthickness=0)
    burger_button.place(x=15, y=110)

    fries_button = Button(frame, image=FriesImg,  command=lambda: open_new_window(snacks_window, fries_window), borderwidth=0, highlightthickness=0)
    fries_button.place(x=215, y=110)

    shawarma_button = Button(frame, image=ShawarmaImg, command=lambda: open_new_window(snacks_window, shawarma_window), borderwidth=0, highlightthickness=0)
    shawarma_button.place(x=15, y=300)

    pizza_button = Button(frame, image=PizzaImg, command=lambda: open_new_window(snacks_window, pizza_window), borderwidth=0, highlightthickness=0)
    pizza_button.place(x=215, y=300)

    siomai_button = Button(frame, image=SiomaImg, command=lambda: open_new_window(snacks_window, siomai_window), borderwidth=0, highlightthickness=0)
    siomai_button.place(x=115, y=500)

    back_button = Button(frame, image=BackImg, command=lambda: open_new_window(snacks_window, second_page), borderwidth=0, highlightthickness=0)
    back_button.place(x=10, y=10)

    snacks_window.mainloop()

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def create_order_window(item_name):
    def confirm_order():
        try:
            quantity = int(quantity_entry.get())
            if quantity > 0:
                price = get_price(item_name)
                add_to_cart(item_name, quantity, price)
                messagebox.showinfo("Order Confirmed", f"You have added {quantity} x {item_name} to the cart.")
            else:
                messagebox.showerror("Invalid Quantity", "Please enter a valid quantity.")
        except ValueError:
            messagebox.showerror("Invalid Quantity", "Please enter a valid quantity.")

    def get_price(item_name):
        prices = {
            "burger": 55.00,
            "fries": 30.00,
            "shawarma": 80.00,
            "pizza": 80.00,
            "siomai": 50.00,
            "coke": 30.00,
            "sprite": 30.00,
            "coke float": 50.00,
            "iced tea": 30.00,
            "pineapple juice": 30.00
        }
        return prices.get(item_name, 0)

    order_window = Tk()
    order_window.title(f"{item_name} Order")
    order_window.geometry("400x715")
    order_window.resizable(False, False)

    background_image = Image.open(r"ayus.png").resize((400, 715))
    background_image = ImageTk.PhotoImage(background_image)

    frame = Frame(order_window)
    frame.pack(fill=BOTH, expand=True)

    canvas1 = Canvas(frame, height=715, width=400, highlightthickness=0)
    canvas1.create_image(0, 0, anchor=NW, image=background_image)
    canvas1_image = background_image
    canvas1.pack(padx=0.1, pady=0.1)

    quantity = IntVar(value=0)

    def increase():
        quantity.set(quantity.get() + 1)

    def decrease():
        if quantity.get() > 1:
            quantity.set(quantity.get() - 1)

    # Back button (left arrow)
    BackImg = ImageTk.PhotoImage(Image.open(r"back button.png").resize((30, 30)))
    back_button = Button(frame, image=BackImg, command=lambda: open_new_window(order_window, second_page), borderwidth=0, highlightthickness=0)
    back_button.place(x=10, y=10)

    # Item label
    item_label = Label(frame, text=item_name.capitalize(), font=("Arial", 24), bg="#FFF")
    item_label.place(x=20, y=200)

    # Price label
    price_label = Label(frame, text=f"₱{get_price(item_name):.2f}", font=("Arial", 20), bg="#FFF")
    price_label.place(x=20, y=250)

    # Quantity selector
    decrease_button = Button(frame, text="-", command=decrease, font=("Arial", 20), bg="black", fg="white")
    decrease_button.place(x=120, y=300, width=50, height=50)

    quantity_entry = Entry(frame, textvariable=quantity, font=("Arial", 20), justify='center')
    quantity_entry.place(x=180, y=300, width=50, height=50)

    increase_button = Button(frame, text="+", command=increase, font=("Arial", 20), bg="black", fg="white")
    increase_button.place(x=240, y=300, width=50, height=50)

    # Confirm button
    confirm_button = Button(frame, text="CONFIRM", font=("Arial", 20), command=confirm_order, bg="white", fg="black")
    confirm_button.place(x=128, y=400)

    order_window.mainloop()

def burger_window():
    create_order_window("burger")

def fries_window():
    create_order_window("fries")

def shawarma_window():
    create_order_window("shawarma")

def pizza_window():
    create_order_window("pizza")

def siomai_window():
    create_order_window("siomai")

def drinks_page():
    drinks_window = Tk()
    drinks_window.title("FFO")
    drinks_window.geometry("400x715")
    drinks_window.resizable(False, False)
    width = 400
    height = 715

    background_image = (Image.open(r"Window_Bg_Drinks(3).png").resize((400, 715)))
    background_image = ImageTk.PhotoImage(background_image)
    CokeImg = ImageTk.PhotoImage(Image.open(r"coke.png").resize((170, 170)))
    SpriteImg = ImageTk.PhotoImage(Image.open(r"sprite.png").resize((170, 170)))
    CokeFloatImg = ImageTk.PhotoImage(Image.open(r"cokefloat.png").resize((170, 170)))
    IcedTeaImg = ImageTk.PhotoImage(Image.open(r"iced tea.png").resize((170, 170)))
    PineappleJuiceImg = ImageTk.PhotoImage(Image.open(r"pineapple.png").resize((170, 170)))
    BackImg = ImageTk.PhotoImage(Image.open(r"back button.png").resize((30, 30)))

    frame = Frame(drinks_window)
    frame.pack(fill=BOTH, expand=True)  # Use BOTH and expand=True to make the frame expand

    # Canvas Image
    canvas1 = Canvas(frame, height=height, width=width, highlightthickness=0)
    canvas1.create_image(0, 0, anchor=NW, image=background_image)
    canvas1.pack(padx=0.1, pady=0.1)

    # Create Buttons
    coke_button = Button(frame, image=CokeImg, command=lambda: open_new_window(drinks_window, coke_window), borderwidth=0, highlightthickness=0)
    coke_button.place(x=15, y=110)

    sprite_button = Button(frame, image=SpriteImg, command=lambda: open_new_window(drinks_window, sprite_window), borderwidth=0, highlightthickness=0)
    sprite_button.place(x=215, y=110)

    cokefloat_button = Button(frame, image=CokeFloatImg, command=lambda: open_new_window(drinks_window, cokefloat_window), borderwidth=0, highlightthickness=0)
    cokefloat_button.place(x=15, y=300)

    icedtea_button = Button(frame, image=IcedTeaImg, command=lambda: open_new_window(drinks_window, icedtea_window), borderwidth=0, highlightthickness=0)
    icedtea_button.place(x=215, y=300)

    pineapplejuice_button = Button(frame, image=PineappleJuiceImg, command=lambda: open_new_window(drinks_window, pineapplejuice_window), borderwidth=0, highlightthickness=0)
    pineapplejuice_button.place(x=115, y=500)

    back_button = Button(frame, image=BackImg, command=lambda: open_new_window(drinks_window, drinks_page), borderwidth=0, highlightthickness=0)
    back_button.place(x=10, y=10)

    drinks_window.mainloop()

def coke_window():
    create_order_window("coke")

def sprite_window():
    create_order_window("sprite")

def cokefloat_window():
    create_order_window("coke float")

def icedtea_window():
    create_order_window("iced tea")

def pineapplejuice_window():
    create_order_window("pineapple juice")

# Initialize the database
initialize_database()
first_page()
