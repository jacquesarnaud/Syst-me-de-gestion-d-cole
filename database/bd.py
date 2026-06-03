import sqlite3

class DatabaseManager:

    def __init__(self):
        self.conn = sqlite3.connect('BASSE.db')
        self.cusor = self.conn.cursor()
        