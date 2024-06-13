import tkinter as tk
from tkinter import messagebox

class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items_by_category(self):
        categories = {}
        for item in self.items:
            if item.category not in categories:
                categories[item.category] = []
            categories[item.category].append(item)
        return categories

class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.name in self.items:
            self.items[item.name]['quantity'] += 1
        else:
            self.items[item.name] = {'item': item, 'quantity': 1}

    def calculate_total(self):
        return sum(details['item'].price * details['quantity'] for details in self.items.values())

    def show_order(self):
        order_details = ""
        for name, details in self.items.items():
            order_details += f"{details['quantity']} x {name} @ ${details['item'].price:.2f} each\n"
        order_details += f"Total: ${self.calculate_total():.2f}"
        return order_details

class FastFoodMachine:
    def __init__(self, root):
        self.menu = Menu()
        self.order = Order()
        self.dine_option = None
        self.root = root
        self.setup_gui()

    def setup_gui(self):
        self.root.title("Fast Food Machine")
        self.root.geometry("300x500")  # Mobile size window

        # Frames for different sections
        self.dine_option_frame = tk.Frame(self.root)
        self.menu_frame = tk.Frame(self.root)
        self.order_frame = tk.Frame(self.root)

        self.dine_option_frame.pack(fill="both", expand=True)

        tk.Label(self.dine_option_frame, text="Quickie Foods", font=("Helvetica", 16, "bold")).pack()

        tk.Label(self.dine_option_frame, text="Choose dining option:").pack(pady=10)

        dine_in_btn = tk.Button(self.dine_option_frame, text="Dine in", width=15, height=3, command=lambda: self.set_dine_option("Dine-in"))
        dine_in_btn.pack(pady=5)

        take_out_btn = tk.Button(self.dine_option_frame, text="Take out", width=15, height=3, command=lambda: self.set_dine_option("Take-out"))
        take_out_btn.pack(pady=5)

    def set_dine_option(self, option):
        self.dine_option = option
        self.dine_option_frame.pack_forget()  # Hide the dine option frame
        self.show_menu()  # Show the menu frame

    def show_menu(self):
        self.menu_frame.pack(fill="both", expand=True)  # Show the menu frame

        tk.Label(self.menu_frame, text=f"Dining option: {self.dine_option}").pack(pady=10)
        tk.Label(self.menu_frame, text="Menu:").pack(pady=10)

        self.item_counter_label = tk.Label(self.menu_frame, text="Order Details:\n")
        self.item_counter_label.pack(pady=10)

        categories = self.menu.get_items_by_category()
        for category, items in categories.items():
            tk.Label(self.menu_frame, text=category, font=('bold')).pack(pady=5)
            for item in items:
                btn = tk.Button(self.menu_frame, text=str(item), command=lambda i=item: self.add_to_order(i))
                btn.pack(pady=5)

        tk.Button(self.menu_frame, text="Show Order", command=self.show_final_order).pack(pady=20)

    def add_to_order(self, item):
        self.order.add_item(item)
        messagebox.showinfo("Item Added", f"{item.name} has been added to your order.")
        self.update_item_counter()

    def update_item_counter(self):
        order_details = "Order Details:\n"
        for name, details in self.order.items.items():
            order_details += f"{details['quantity']} x {name} @ ${details['item'].price:.2f} each\n"
        order_details += f"Total: ${self.order.calculate_total():.2f}"
        self.item_counter_label.config(text=order_details)

    def add_menu_item(self, name, price, category):
        item = MenuItem(name, price, category)
        self.menu.add_item(item)

    def show_final_order(self):
        order_details = self.order.show_order()
        messagebox.showinfo("Final Order", f"Your order ({self.dine_option}):\n{order_details}")

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    machine = FastFoodMachine(root)
    machine.add_menu_item("Burger", 5.99, "Sandwich & Burgers")
    machine.add_menu_item("Fries", 2.49, "Sandwich & Burgers")
    machine.add_menu_item("Soda", 1.99, "Meals")
    machine.add_menu_item("Chicken Meal", 7.99, "Meals")
    root.mainloop()