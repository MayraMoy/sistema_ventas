import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('mi_inventario.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Productos(
        codigo_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion TEXT UNIQUE NOT NULL, 
        existentes_iniciales INTEGER NOT NULL,
        entradas INTEGER NOT NULL,
        salidas INTEGER NOT NULL,
        stock INTEGER NOT NULL
    )
''')

conn.commit()
conn.close()

class Productos:
    def __init__(self):
        conn = sqlite3.connect('mi_inventario.db')
        cursor = conn.cursor()
    
    def mostrar_productos(self):
        cursor.execute("SELECT * FROM Productos")
        productos = cursor.fetchall()
        
        return productos
    
    def agregar_producto(self, descripcion, existentes_iniciales, entradas, salidas, stock):
        cursor.execute("INSERT INTO Productos (descripcion, existentes_iniciales, entradas, salidas, stock) VALUES (?, ?, ?, ?, ?)")
        conn.commit()
        
        messagebox.showinfo('Sistema de Ventas', 'Producto agregado correctamente')
        
    def buscar_producto(self, descripcion):
        cursor.execute("SELECT * FROM Productos WHERE descripcion = ?", (descripcion,))
        producto = cursor.fetchone()
        messagebox.showinfo('Sistema de Ventas', 'Producto encontrado correctamentte')
        return producto
    
    def actualizar_producto(self, descripcion, existentes_iniciales, entradas, salidas, stock):
        cursor.execute("UPDATE Productos SET existentes_iniciales = ?, entradas = ?, salidas = ?, stock = ? WHERE descipcion = ?", (existentes_iniciales, entradas, salidas, stock, descripcion))
        conn.commit()
        messagebox.showinfo('Sistema de Ventas', 'Producto actualizado correctamente')
    
    def eliminar_producto(self, descipcion):
        cursor.execute("DELETE FROM Productos WHERE descripcion = ?", (descipcion,))
        conn.commit()
        messagebox.showinfo('Sistema de Ventas', 'Producto eliminado correctamente')
    
    def close_connection(self):
        self.conn.close()