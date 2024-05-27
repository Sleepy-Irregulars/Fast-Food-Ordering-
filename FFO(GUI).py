import tkinter as tk
from tkinter import messagebox

def place_order():
    order = "Your order:\n"
    if burger_var.get():
        order += "Burger\n"
    if fries_var.get():
        order += "Fries\n"
    if drink_var.get():
        order += "Drink\n"
    messagebox.showinfo("Order Confirmation", order)

root = tk.Tk()
root.title("Fast Food Ordering System")

burger_var = tk.BooleanVar()
fries_var = tk.BooleanVar()
drink_var = tk.BooleanVar()

tk.Label(root, text="Menu").pack()
tk.Checkbutton(root, text="Burger", variable=burger_var).pack()
tk.Checkbutton(root, text="Fries", variable=fries_var).pack()
tk.Checkbutton(root, text="Drink", variable=drink_var).pack()

tk.Button(root, text="Place Order", command=place_order).pack()

root.mainloop()
