import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('mi_productos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Articulos(
        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion TEXT UNIQUE NOT NULL, 
        precio REAL NOT NULL,
        unidad INTEGER NOT NULL,
        total INTEGER NOT NULL,
    )
''')

conn.commit()
conn.close()

class Articulos:
    def __init__(self, root):
        self.root = root
        