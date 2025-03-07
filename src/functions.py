import sqlite3
import hashlib
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usser TEXT UNIQUE NOT NULL, 
        password_hash TEXT NOT NULL
    )
''')

admin_password = hashlib.sha256("A9X3-7B2C5".encode()).hexdigest()
cursor.execute("SELECT * FROM Usuarios WHERE usser = 'admin'")
if not cursor.fetchone(): 
    cursor.execute("INSERT INTO Usuarios (usser, password_hash) VALUES (?, ?)", ("admin", admin_password))

conn.commit()
conn.close()


class Functions:
    def __init__(self):
        self.conn = sqlite3.connect('mi_base_de_datos.db')
        self.cursor = self.conn.cursor()

    def Enter(self, username, password):
        self.cursor.execute("SELECT password_hash FROM Usuarios WHERE usser = ?", (username,))
        row = self.cursor.fetchone()
        if row:
            stored_hash = row[0]
            if stored_hash == hashlib.sha256(password.encode()).hexdigest():
                messagebox.showinfo('Sistema Ventas','Iniciando sesion al sistema...')
                return True
            else:
                messagebox.showerror('Error', 'Contraseña Incorrecta')
                return False
        else:
            messagebox.showerror('Error', 'Usuario no encontrado')
            return False

    def close_connection(self):
        self.conn.close()


