import tkinter as tk
from tkinter import Tk, Frame
from tkinter.font import Font
from src.functions import Functions

class Manager:
    def __init__(self, root):
        self.root = root
        self.root.title('Sistema de Gestion de Ventas')
        self.root.geometry('600x500')
        self.root.configure(bg='#375b76')
        
        self.frame = tk.Frame(self.root, padx=100, pady=80, bg='#ffffff')
        self.frame.place(relx=0.5, rely=0.5, anchor='center')
        
        self.tipografia_subtitulo = Font(family="Poppins", size=20)
        self.boton_entrar = Font(family="Poppins", size=12)
        self.boton_registrar = Font(family="Poppins", size=12, underline=True)
        
        self.label = tk.Label(self.frame, text='Bienvenido de Nuevo', font=self.tipografia_subtitulo, bg='#FFFFFF')
        self.label.grid(row=0, column=0, columnspan=2, pady=10)
        
        self.label_user = tk.Label(self.frame,text="👤", font=("Arial", 14), bg="white")
        self.label_user.grid(row=1, column=0, padx=5, pady=5)
        entry_user = tk.Entry(self.frame, width=25, font=("Arial", 12))
        entry_user.grid(row=1, column=1, pady=5)

        self.label_password = tk.Label(self.frame, text="🔒", font=("Arial", 14), bg="white")
        self.label_password.grid(row=2, column=0, padx=5, pady=5)
        entry_pass = tk.Entry(self.frame, width=25, font=("Arial", 12), show="*")
        entry_pass.grid(row=2, column=1, pady=5)
        
        btn_entrar = tk.Button(self.frame, text="Entrar", font=self.boton_entrar, bg="#00bf63", fg="black", width=15, command=self.enter)
        btn_entrar.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.functions = Functions()
        
    def enter(self):
        username = self.entry_user.get()
        password = self.entry_pass.get()
        self.functions.Enter(username, password)

