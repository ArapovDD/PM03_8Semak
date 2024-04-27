Иноформационная система была сделанна в рамках производственной практики ПМ.03
Стек:
Python(Библиотеки: Tkinter, sqlite3).
СУБД: SQlite 3
БД:
-- Таблица Menu
CREATE TABLE Menu (
    ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    ItemName TEXT NOT NULL,
    Description TEXT,
    Price REAL NOT NULL
);

-- Таблица Orders
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER,
    ItemID INTEGER,
    Quantity INTEGER NOT NULL,
    OrderTime TEXT NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ItemID) REFERENCES Menu(ItemID)
);

-- Таблица Customers
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    PhoneNumber TEXT,
    Email TEXT
);

-- Таблица Staff
CREATE TABLE Staff (
    StaffID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Position TEXT NOT NULL,
    PhoneNumber TEXT,
    Email TEXT
);

-- Таблица UserAccounts
CREATE TABLE UserAccounts (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    Password TEXT NOT NULL,
    Role TEXT NOT NULL
);
--------------
перевод на рус для понимния
-- Таблица Меню
CREATE TABLE Меню (
    ID_Блюда INTEGER PRIMARY KEY AUTOINCREMENT,
    Название_Блюда TEXT NOT NULL,
    Описание TEXT,
    Цена REAL NOT NULL
);

-- Таблица Заказы
CREATE TABLE Заказы (
    ID_Заказа INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Клиента INTEGER,
    ID_Блюда INTEGER,
    Количество INTEGER NOT NULL,
    Время_Заказа TEXT NOT NULL,
    FOREIGN KEY (ID_Клиента) REFERENCES Клиенты(ID_Клиента),
    FOREIGN KEY (ID_Блюда) REFERENCES Меню(ID_Блюда)
);

-- Таблица Клиенты
CREATE TABLE Клиенты (
    ID_Клиента INTEGER PRIMARY KEY AUTOINCREMENT,
    Имя TEXT NOT NULL,
    Фамилия TEXT NOT NULL,
    Телефон TEXT,
    Email TEXT
);

-- Таблица Персонал
CREATE TABLE Персонал (
    ID_Персонала INTEGER PRIMARY KEY AUTOINCREMENT,
    Имя TEXT NOT NULL,
    Фамилия TEXT NOT NULL,
    Должность TEXT NOT NULL,
    Телефон TEXT,
    Email TEXT
);

-- Таблица Учетные_Записи
CREATE TABLE Учетные_Записи (
    ID_Пользователя INTEGER PRIMARY KEY AUTOINCREMENT,
    Имя_Пользователя TEXT NOT NULL,
    Пароль TEXT NOT NULL,
    Роль TEXT NOT NULL
);
--------------------
Лдано вот ещё записи 
-- Записи для таблицы Menu
INSERT INTO Menu (ItemName, Description, Price) VALUES ('Пицца Маргарита', 'Томатный соус, моцарелла, базилик', 500);
INSERT INTO Menu (ItemName, Description, Price) VALUES ('Паста Карбонара', 'Спагетти, гуанчиале, яйцо, пармезан', 400);
INSERT INTO Menu (ItemName, Description, Price) VALUES ('Тирамису', 'Десерт с маскарпоне и кофе', 300);
INSERT INTO Menu (ItemName, Description, Price) VALUES ('Ризотто с грибами', 'Рис, грибы, пармезан', 450);
INSERT INTO Menu (ItemName, Description, Price) VALUES ('Карпаччо', 'Тонко нарезанное мясо', 350);

-- Записи для таблицы Orders
INSERT INTO Orders (CustomerID, ItemID, Quantity, OrderTime) VALUES (1, 1, 2, '2024-04-27 13:00:00');
INSERT INTO Orders (CustomerID, ItemID, Quantity, OrderTime) VALUES (2, 2, 1, '2024-04-27 13:15:00');
INSERT INTO Orders (CustomerID, ItemID, Quantity, OrderTime) VALUES (3, 3, 1, '2024-04-27 13:30:00');
INSERT INTO Orders (CustomerID, ItemID, Quantity, OrderTime) VALUES (4, 4, 1, '2024-04-27 13:45:00');
INSERT INTO Orders (CustomerID, ItemID, Quantity, OrderTime) VALUES (5, 5, 1, '2024-04-27 14:00:00');

-- Записи для таблицы Customers
INSERT INTO Customers (FirstName, LastName, PhoneNumber, Email) VALUES ('Иван', 'Иванов', '+79001234567', 'ivanov@example.com');
INSERT INTO Customers (FirstName, LastName, PhoneNumber, Email) VALUES ('Петр', 'Петров', '+79007654321', 'petrov@example.com');
INSERT INTO Customers (FirstName, LastName, PhoneNumber, Email) VALUES ('Сергей', 'Сергеев', '+79009876543', 'sergeev@example.com');
INSERT INTO Customers (FirstName, LastName, PhoneNumber, Email) VALUES ('Анна', 'Аннова', '+79005432198', 'annova@example.com');
INSERT INTO Customers (FirstName, LastName, PhoneNumber, Email) VALUES ('Мария', 'Мариева', '+79003216549', 'marieva@example.com');

-- Записи для таблицы Staff
INSERT INTO Staff (FirstName, LastName, Position, PhoneNumber, Email) VALUES ('Алексей', 'Алексеев', 'Официант', '+79006543219', 'alexeev@example.com');
INSERT INTO Staff (FirstName, LastName, Position, PhoneNumber, Email) VALUES ('Виктор', 'Викторов', 'Повар', '+79008765432', 'viktorov@example.com');
INSERT INTO Staff (FirstName, LastName, Position, PhoneNumber, Email) VALUES ('Елена', 'Еленова', 'Бармен', '+79004321987', 'elenova@example.com');
INSERT INTO Staff (FirstName, LastName, Position, PhoneNumber, Email) VALUES ('Николай', 'Николаев', 'Официант', '+79002198765', 'nikolaev@example.com');
INSERT INTO Staff (FirstName, LastName, Position, PhoneNumber, Email) VALUES ('Ольга', 'Ольгова', 'Повар', '+79009876543', 'olgova@example.com');
