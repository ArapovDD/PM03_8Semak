# database_connector.py

import sqlite3

class DatabaseConnector:
    def __init__(self):
        self.db_name = 'ArapovPM03.db' 

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()
