# BuCustomers.py

import tkinter as tk
from database_connector import DatabaseConnector

class AddCustomerWindow:
    def __init__(self, root, customers_window):
        self.root = root
        self.root.geometry('400x200')
        self.customers_window = customers_window

        self.create_widgets()

    def create_widgets(self):
        self.first_name_label = tk.Label(self.root, text='Имя:')
        self.first_name_label.pack()
        self.first_name_entry = tk.Entry(self.root)
        self.first_name_entry.pack(fill='x')

        self.last_name_label = tk.Label(self.root, text='Фамилия:')
        self.last_name_label.pack()
        self.last_name_entry = tk.Entry(self.root)
        self.last_name_entry.pack(fill='x')

        self.phone_number_label = tk.Label(self.root, text='Номер телефона:')
        self.phone_number_label.pack()
        self.phone_number_entry = tk.Entry(self.root)
        self.phone_number_entry.pack(fill='x')

        self.email_label = tk.Label(self.root, text='Email:')
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(fill='x')

        self.add_button = tk.Button(self.root, text='Добавить', command=self.add_customer)
        self.add_button.pack(fill='x')

    def add_customer(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()

        self.customers_window.db.cursor.execute('INSERT INTO Customers (FirstName, LastName, PhoneNumber, Email) VALUES (?, ?, ?, ?)', (first_name, last_name, phone_number, email))
        self.customers_window.db.conn.commit()

        self.customers_window.load_data()
        self.root.destroy()


class CustomersWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Клиенты')
        self.root.geometry('400x200')

        self.db = DatabaseConnector()
        self.db.connect()

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(side='left', fill='both', expand=True)

        self.add_button = tk.Button(self.root, text='Добавить', command=self.open_add_customer_window)
        self.add_button.pack(fill='x')

        self.delete_button = tk.Button(self.root, text='Удалить', command=self.delete_customer)
        self.delete_button.pack(fill='x')

    def load_data(self):
        self.listbox.delete(0, 'end')

        self.db.cursor.execute('SELECT * FROM Customers')
        for row in self.db.cursor.fetchall():
            self.listbox.insert('end', row)

    def open_add_customer_window(self):
        new_window = tk.Toplevel(self.root)
        AddCustomerWindow(new_window, self)

    def delete_customer(self):
        selected_customer = self.listbox.curselection()
        if selected_customer:
            customer_id = self.listbox.get(selected_customer)[0]
            self.db.cursor.execute('DELETE FROM Customers WHERE CustomerID = ?', (customer_id,))
            self.db.conn.commit()
            self.load_data()

    def run(self):
        self.root.mainloop()
