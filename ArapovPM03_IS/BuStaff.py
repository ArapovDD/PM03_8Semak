# BuStaff.py

import tkinter as tk
from database_connector import DatabaseConnector

class AddStaffWindow:
    def __init__(self, root, staff_window):
        self.root = root
        self.root.geometry('400x200')
        self.staff_window = staff_window

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

        self.position_label = tk.Label(self.root, text='Должность:')
        self.position_label.pack()
        self.position_entry = tk.Entry(self.root)
        self.position_entry.pack(fill='x')

        self.phone_number_label = tk.Label(self.root, text='Номер телефона:')
        self.phone_number_label.pack()
        self.phone_number_entry = tk.Entry(self.root)
        self.phone_number_entry.pack(fill='x')

        self.email_label = tk.Label(self.root, text='Email:')
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(fill='x')

        self.add_button = tk.Button(self.root, text='Добавить', command=self.add_staff)
        self.add_button.pack(fill='x')

    def add_staff(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        position = self.position_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()

        self.staff_window.db.cursor.execute('INSERT INTO Staff (FirstName, LastName, Position, PhoneNumber, Email) VALUES (?, ?, ?, ?, ?)', (first_name, last_name, position, phone_number, email))
        self.staff_window.db.conn.commit()

        self.staff_window.load_data()
        self.root.destroy()


class StaffWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Персонал')
        self.root.geometry('400x200')

        self.db = DatabaseConnector()
        self.db.connect()

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(side='left', fill='both', expand=True)

        self.add_button = tk.Button(self.root, text='Добавить', command=self.open_add_staff_window)
        self.add_button.pack(fill='x')

        self.delete_button = tk.Button(self.root, text='Удалить', command=self.delete_staff)
        self.delete_button.pack(fill='x')

    def load_data(self):
        self.listbox.delete(0, 'end')

        self.db.cursor.execute('SELECT * FROM Staff')
        for row in self.db.cursor.fetchall():
            self.listbox.insert('end', row)

    def open_add_staff_window(self):
        new_window = tk.Toplevel(self.root)
        AddStaffWindow(new_window, self)

    def delete_staff(self):
        selected_staff = self.listbox.curselection()
        if selected_staff:
            staff_id = self.listbox.get(selected_staff)[0]
            self.db.cursor.execute('DELETE FROM Staff WHERE StaffID = ?', (staff_id,))
            self.db.conn.commit()
            self.load_data()

    def run(self):
        self.root.mainloop()
