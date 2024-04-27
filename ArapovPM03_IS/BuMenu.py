# BuMenu.py

import tkinter as tk
from database_connector import DatabaseConnector

class AddItemWindow:
    def __init__(self, root, menu_window):
        self.root = root
        self.root.geometry('400x200')  # Установите размер окна
        self.menu_window = menu_window

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.root, text='Название:')
        self.name_label.pack()

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(fill='x')  # Растягивайте поле ввода по горизонтали

        self.description_label = tk.Label(self.root, text='Описание:')
        self.description_label.pack()

        self.description_entry = tk.Entry(self.root)
        self.description_entry.pack(fill='x')  # Растягивайте поле ввода по горизонтали

        self.price_label = tk.Label(self.root, text='Цена:')
        self.price_label.pack()

        self.price_entry = tk.Entry(self.root)
        self.price_entry.pack(fill='x')  # Растягивайте поле ввода по горизонтали

        self.add_button = tk.Button(self.root, text='Добавить', command=self.add_item)
        self.add_button.pack(fill='x')  # Растягивайте кнопку по горизонтали

    def add_item(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        price = self.price_entry.get()

        self.menu_window.db.cursor.execute('INSERT INTO Menu (ItemName, Description, Price) VALUES (?, ?, ?)', (name, description, price))
        self.menu_window.db.conn.commit()

        self.menu_window.load_data()

        self.root.destroy()


class MenuWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Меню')

        self.db = DatabaseConnector()
        self.db.connect()

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(side='left', fill='both', expand=True)

        self.add_button = tk.Button(self.root, text='Добавить', command=self.open_add_item_window)
        self.add_button.pack(fill='x')  # Растягивайте кнопку по горизонтали

        self.delete_button = tk.Button(self.root, text='Удалить', command=self.delete_item)
        self.delete_button.pack(fill='x')  # Растягивайте кнопку по горизонтали

    def load_data(self):
        self.listbox.delete(0, 'end')

        self.db.cursor.execute('SELECT * FROM Menu')
        for row in self.db.cursor.fetchall():
            self.listbox.insert('end', row)

    def open_add_item_window(self):
        new_window = tk.Toplevel(self.root)
        AddItemWindow(new_window, self)

    def delete_item(self):
        selected_item = self.listbox.curselection()
        if selected_item:
            item_id = self.listbox.get(selected_item)[0]
            self.db.cursor.execute('DELETE FROM Menu WHERE ItemID = ?', (item_id,))
            self.db.conn.commit()
            self.load_data()

    def run(self):
        self.root.mainloop()
