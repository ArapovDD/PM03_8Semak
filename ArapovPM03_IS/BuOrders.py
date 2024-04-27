# BuOrders.py

import tkinter as tk
from database_connector import DatabaseConnector

class AddOrderWindow:
    def __init__(self, root, orders_window):
        self.root = root
        self.root.geometry('400x200')
        self.orders_window = orders_window

        self.create_widgets()

    def create_widgets(self):
        self.customer_id_label = tk.Label(self.root, text='ID клиента:')
        self.customer_id_label.pack()
        self.customer_id_entry = tk.Entry(self.root)
        self.customer_id_entry.pack(fill='x')

        self.item_id_label = tk.Label(self.root, text='ID товара:')
        self.item_id_label.pack()
        self.item_id_entry = tk.Entry(self.root)
        self.item_id_entry.pack(fill='x')

        self.quantity_label = tk.Label(self.root, text='Количество:')
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack(fill='x')

        self.order_time_label = tk.Label(self.root, text='Время заказа:')
        self.order_time_label.pack()
        self.order_time_entry = tk.Entry(self.root)
        self.order_time_entry.pack(fill='x')

        self.add_button = tk.Button(self.root, text='Добавить', command=self.add_order)
        self.add_button.pack(fill='x')

    def add_order(self):
        customer_id = self.customer_id_entry.get()
        item_id = self.item_id_entry.get()
        quantity = self.quantity_entry.get()
        order_time = self.order_time_entry.get()

        self.orders_window.db.cursor.execute('INSERT INTO Orders (CustomerID, ItemID, Quantity, OrderTime) VALUES (?, ?, ?, ?)', (customer_id, item_id, quantity, order_time))
        self.orders_window.db.conn.commit()

        self.orders_window.load_data()
        self.root.destroy()


class OrdersWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Заказы')
        self.root.geometry('400x200')

        self.db = DatabaseConnector()
        self.db.connect()

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(side='left', fill='both', expand=True)

        self.add_button = tk.Button(self.root, text='Добавить', command=self.open_add_order_window)
        self.add_button.pack(fill='x')

        self.delete_button = tk.Button(self.root, text='Удалить', command=self.delete_order)
        self.delete_button.pack(fill='x')

    def load_data(self):
        self.listbox.delete(0, 'end')

        self.db.cursor.execute('SELECT * FROM Orders')
        for row in self.db.cursor.fetchall():
            self.listbox.insert('end', row)

    def open_add_order_window(self):
        new_window = tk.Toplevel(self.root)
        AddOrderWindow(new_window, self)

    def delete_order(self):
        selected_order = self.listbox.curselection()
        if selected_order:
            order_id = self.listbox.get(selected_order)[0]
            self.db.cursor.execute('DELETE FROM Orders WHERE OrderID = ?', (order_id,))
            self.db.conn.commit()
            self.load_data()

    def run(self):
        self.root.mainloop()
