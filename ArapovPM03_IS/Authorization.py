# Authorization.py

import tkinter as tk
from tkinter import messagebox
from database_connector import DatabaseConnector

class RegistrationWindow:
    def __init__(self, root, auth_window):
        self.root = root
        self.root.geometry('400x200')
        self.auth_window = auth_window

        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self.root, text='Имя пользователя:')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(fill='x')

        self.password_label = tk.Label(self.root, text='Пароль:')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack(fill='x')

        self.role_label = tk.Label(self.root, text='Роль:')
        self.role_label.pack()
        self.role_entry = tk.Entry(self.root)
        self.role_entry.pack(fill='x')

        self.register_button = tk.Button(self.root, text='Регистрация', command=self.register)
        self.register_button.pack(fill='x')

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_entry.get()

        if not username or not password or not role:
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
            return

        self.auth_window.db.cursor.execute('SELECT * FROM UserAccounts WHERE Username = ?', (username,))
        user = self.auth_window.db.cursor.fetchone()
        if user is not None:
            messagebox.showerror("Ошибка", "Пользователь с таким именем уже существует!")
            return

        self.auth_window.db.cursor.execute('INSERT INTO UserAccounts (Username, Password, Role) VALUES (?, ?, ?)', (username, password, role))
        self.auth_window.db.conn.commit()

        messagebox.showinfo("Успех", "Регистрация прошла успешно!")
        self.root.destroy()
        self.auth_window.open_main_window()

class AuthorizationWindow:
    def __init__(self, root, main_window_class):
        self.root = root
        self.root.title('Авторизация')
        self.root.geometry('400x200')

        self.db = DatabaseConnector()
        self.db.connect()

        self.main_window_class = main_window_class

        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self.root, text='Имя пользователя:')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(fill='x')

        self.password_label = tk.Label(self.root, text='Пароль:')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack(fill='x')

        self.login_button = tk.Button(self.root, text='Войти', command=self.login)
        self.login_button.pack(fill='x')

        self.register_button = tk.Button(self.root, text='Регистрация', command=self.open_registration_window)
        self.register_button.pack(fill='x')

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        self.db.cursor.execute('SELECT * FROM UserAccounts WHERE Username = ? AND Password = ?', (username, password))
        user = self.db.cursor.fetchone()

        if user is not None:
            messagebox.showinfo("Успех", "Авторизация прошла успешно!")
            self.open_main_window()
        else:
            messagebox.showerror("Ошибка", "Неверное имя пользователя или пароль!")

    def open_registration_window(self):
        new_window = tk.Toplevel(self.root)
        RegistrationWindow(new_window, self)

    def open_main_window(self):
        self.root.destroy()
        new_root = tk.Tk()
        self.main_window_class(new_root)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    from main import MainWindow
    app = AuthorizationWindow(root, MainWindow)
    app.run()
