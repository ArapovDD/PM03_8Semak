# main.py

import tkinter as tk
from database_connector import DatabaseConnector
from BuMenu import MenuWindow
from BuOrders import OrdersWindow
from BuCustomers import CustomersWindow
from BuStaff import StaffWindow
from Authorization import AuthorizationWindow

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Информационная система ресторана')
        self.root.geometry('600x400')

        self.db = DatabaseConnector()
        self.db.connect()

        self.create_widgets()

    def create_widgets(self):
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill='x')

        self.menu_button = tk.Button(self.button_frame, text='Меню', command=self.open_menu)
        self.menu_button.pack(side='left', fill='x', expand=True)

        self.orders_button = tk.Button(self.button_frame, text='Заказы', command=self.open_orders)
        self.orders_button.pack(side='left', fill='x', expand=True)

        self.customers_button = tk.Button(self.button_frame, text='Клиенты', command=self.open_customers)
        self.customers_button.pack(side='left', fill='x', expand=True)

        self.staff_button = tk.Button(self.button_frame, text='Персонал', command=self.open_staff)
        self.staff_button.pack(side='left', fill='x', expand=True)

    def open_menu(self):
        new_window = tk.Toplevel(self.root)
        MenuWindow(new_window)

    def open_orders(self):
        new_window = tk.Toplevel(self.root)
        OrdersWindow(new_window)

    def open_customers(self):
        new_window = tk.Toplevel(self.root)
        CustomersWindow(new_window)

    def open_staff(self):
        new_window = tk.Toplevel(self.root)
        StaffWindow(new_window)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = AuthorizationWindow(root, MainWindow)  # Передайте MainWindow как аргумент
    app.run()
