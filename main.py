from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

# Function to establish a connection to the SQLite database
def connect_to_database():
    try:
        connection = sqlite3.connect("ffo_database.db")
        return connection
    except sqlite3.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

# Function to initialize the database tables
def initialize_database():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS menu (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              item_name TEXT,
                              price REAL)''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              order_type TEXT,
                              item_name TEXT,
                              quantity INTEGER,
                              order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS weekly_deals (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              deal_name TEXT,
                              price REAL,
                              description TEXT)''')

            cursor.execute('''DELETE FROM menu''')
            cursor.executemany("INSERT INTO menu (item_name, price) VALUES (?, ?)", [
                ("Yumburger", 40.00),
                ("Fried Chicken", 100.00),
                ("Spaghetti", 50.00),
                ("Jolly Hotdog", 50.00),
                ("Palabok Fiesta", 100.00),
                ("Burger Steak", 80.00),
                ("Chickenjoy Bucket", 569.00),
                ("Jolly Spaghetti", 100.00),
                ("Halo-Halo", 60.00)
            ])

            cursor.execute('''DELETE FROM weekly_deals''')
            cursor.executemany("INSERT INTO weekly_deals (deal_name, price, description) VALUES (?, ?, ?)", [
                ("Yumburger Promo", 30, "Get a Yumburger for only ₱30.00"),
                ("Fried Chicken Deal", 99, "Special price for fried chicken."),
                ("Spaghetti Fiesta", 150, "Enjoy our spaghetti at a reduced price."),
                ("Hotdog Combo", 50, "Jolly Hotdog with fries and drink."),
                ("Palabok Special", 200, "Palabok Fiesta with extra toppings.")
            ])

            connection.commit()
        except sqlite3.Error as err:
            messagebox.showerror("Error", f"Failed to initialize database: {err}")
        finally:
            cursor.close()
            connection.close()

# Function to place an order
def place_order(item_name, quantity, order_type):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO orders (order_type, item_name, quantity) VALUES (?, ?, ?)", (order_type, item_name, quantity))
            connection.commit()
            messagebox.showinfo("Order Placed", f"Your order for {quantity} x {item_name} has been placed successfully!")
        except sqlite3.Error as err:
            messagebox.showerror("Error", f"Failed to place order: {err}")
        finally:
            cursor.close()
            connection.close()

# Function to show order dialog
def order_item(item_name, order_type):
    order_window = Toplevel(root)
    order_window.title(f"Order {item_name}")
    order_window.geometry("300x250")

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT price FROM menu WHERE item_name = ?", (item_name,))
            price = cursor.fetchone()[0]
        except sqlite3.Error as err:
            messagebox.showerror("Error", f"Failed to fetch price: {err}")
            cursor.close()
            connection.close()
            return

    lbl_quantity = Label(order_window, text="Quantity:")
    lbl_quantity.pack(pady=10)
    quantity_var = IntVar(value=1)
    quantity_entry = Entry(order_window, textvariable=quantity_var)
    quantity_entry.pack(pady=10)

    lbl_total_price = Label(order_window, text="Total Price: ₱0.00")
    lbl_total_price.pack(pady=10)

    def update_total_price(*args):
        try:
            quantity = int(quantity_var.get())
            total_price = quantity * price
            lbl_total_price.config(text=f"Total Price: ₱{total_price:.2f}")
        except ValueError:
            lbl_total_price.config(text="Total Price: ₱0.00")

    quantity_var.trace("w", update_total_price)

    def confirm_order():
        try:
            quantity = int(quantity_var.get())
            if quantity > 0:
                place_order(item_name, quantity, order_type)
                order_window.destroy()
            else:
                messagebox.showerror("Invalid Quantity", "Quantity must be greater than 0")
        except ValueError:
            messagebox.showerror("Invalid Quantity", "Quantity must be a positive integer")

    btn_confirm = Button(order_window, text="Confirm Order", command=confirm_order)
    btn_confirm.pack(pady=10)

# Function to show the menu list
def show_menu(order_type):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM menu")
            rows = cursor.fetchall()
            menu_window = Toplevel(root)
            menu_window.title("Menu List")
            menu_window.geometry("400x724")

            # Load the background image
            background_image = Image.open("background1.png")
            background_photo = ImageTk.PhotoImage(background_image)

            # Create a label with the background image
            background_label = Label(menu_window, image=background_photo)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            # Create a frame for the menu items
            menu_frame = Frame(menu_window)
            menu_frame.pack(fill="both", expand=True, pady=50)  # Adjust the padding as needed

            for row in rows:
                item_name = row[1]
                item_price = row[2]
                item_frame = Frame(menu_frame)
                item_frame.pack(fill="x", pady=5)
                lbl_item = Label(item_frame, text=f"{item_name}: ₱{item_price:.2f}")
                lbl_item.pack(side="left")
                btn_order = Button(item_frame, text="Order", command=lambda name=item_name: order_item(name, order_type))
                btn_order.pack(side="right")

            # Keep a reference to the image to prevent garbage collection
            background_label.image = background_photo
        except sqlite3.Error as err:
            messagebox.showerror("Error", f"Failed to fetch menu: {err}")
        finally:
            cursor.close()
            connection.close()


# Function to show the best sellers
def show_best_sellers(order_type):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT item_name, COUNT(*) AS count FROM orders GROUP BY item_name ORDER BY count DESC LIMIT 5")
            rows = cursor.fetchall()
            best_sellers_window = Toplevel(root)
            best_sellers_window.title("Best Sellers")
            best_sellers_window.geometry("300x300")

            for row in rows:
                item_name = row[0]
                item_count = row[1]
                item_frame = Frame(best_sellers_window)
                item_frame.pack(fill="x", pady=5)
                lbl_item = Label(item_frame, text=f"{item_name}: {item_count} orders")
                lbl_item.pack(side="left")
                btn_order = Button(item_frame, text="Order", command=lambda name=item_name: order_item(name, order_type))
                btn_order.pack(side="right")
        except sqlite3.Error as err:
            messagebox.showerror("Error", f"Failed to fetch best sellers: {err}")
        finally:
            cursor.close()
            connection.close()

# Function to show weekly deals
def show_weekly_deals(order_type):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM weekly_deals")
            rows = cursor.fetchall()
            deals_window = Toplevel(root)
            deals_window.title("Weekly Deals")
            deals_window.geometry("400x400")

            for row in rows:
                deal_name = row[1]
                deal_price = row[2]
                deal_description = row[3]
                item_frame = Frame(deals_window)
                item_frame.pack(fill="x", pady=5)
                lbl_item = Label(item_frame, text=f"{deal_name}: ₱{deal_price:.2f} - {deal_description}")
                lbl_item.pack(side="left")
                btn_order = Button(item_frame, text="Order", command=lambda name=deal_name: order_item(name, order_type))
                btn_order.pack(side="right")
        except sqlite3.Error as err:
            messagebox.showerror("Error", f"Failed to fetch weekly deals: {err}")
        finally:
            cursor.close()
            connection.close()

# Function to create dine-in or take-out window
def create_order_window(order_type):
    order_window = Toplevel(root)
    order_window.title(f"{order_type} Options")
    order_window.geometry("400x724")

    # Load the background image
    background_image = Image.open("background1.png")
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label with the background image
    background_label = Label(order_window, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Calculate the vertical position for the buttons
    window_height = order_window.winfo_reqheight()
    button_height = 50  # Adjust button height here
    spacing = 0.1  # Adjust spacing between buttons here
    total_button_height = 3 * button_height + 2 * spacing
    vertical_offset = (window_height - total_button_height) // 2

    # Place the buttons vertically centered
    menu_button = Button(order_window, text="Menu List", command=lambda: show_menu(order_type), width=15, height=3)  # Adjust width and height here
    menu_button.place(relx=0.5, rely=vertical_offset / window_height, anchor="n")

    best_sellers_button = Button(order_window, text="Best Sellers", command=lambda: show_best_sellers(order_type), width=15, height=3)  # Adjust width and height here
    best_sellers_button.place(relx=0.5, rely=(vertical_offset + button_height + spacing) / window_height, anchor="n")

    weekly_deals_button = Button(order_window, text="Weekly Deals", command=lambda: show_weekly_deals(order_type), width=15, height=3)  # Adjust width and height here
    weekly_deals_button.place(relx=0.5, rely=(vertical_offset + 2 * button_height + 2 * spacing) / window_height, anchor="n")

    # Keep a reference to the image to prevent garbage collection
    background_label.image = background_photo



root = Tk()
root.title("FFO")
root.geometry("400x724")
# root.iconbitmap("PNCLogo.ico")
image_0 = Image.open(r"background1.png")
bck_end = ImageTk.PhotoImage(image_0)
lbl = Label(root, image=bck_end)
lbl.grid(row=0, column=0)
root.resizable(False, False)

# Creating a photoimage object to use image
photo1 = PhotoImage(file=r"dine in.png")
photo2 = PhotoImage(file=r"take out.png")

# Resizing image to fit on button
photo1_resized = photo1.subsample(3, 3)
photo2_resized = photo2.subsample(3, 3)

# Button1
DineInButton = Button(root, text=" ", image=photo1_resized, command=lambda: create_order_window("Dine-In"))
DineInButton.place(relx=0.5, rely=0.3, anchor=CENTER)

# Button2
TakeOutButton = Button(root, text=" ", image=photo2_resized, command=lambda: create_order_window("Take-Out"))
TakeOutButton.place(relx=0.5, rely=0.6, anchor=CENTER)

# Initialize the database with the menu and weekly deals
initialize_database()

# Start the main event loop
root.mainloop()
