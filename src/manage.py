import tkinter as tk
from tkinter import Tk, Frame
from tkinter.font import Font
from src.functions import Functions

class Manager:
    def __init__(self, root):
        self.root = root
        self.root.title('Sistema de Gestion de Ventas')
        
        # ------------------------------------------------------------------------
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 600
        window_height = 500                                  # Centra la ventana en la pantalla

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}") # Centrada
        self.root.configure(bg='#375b76')
        
        # ----------------------------------------------------------------
        self.frame = tk.Frame(self.root, padx=100, pady=80, bg='#ffffff')
        self.frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Configuracion de la tipografia
        self.subtitle_typography = Font(family="Poppins", size=20)
        self.enter_button = Font(family="Poppins", size=12)
        self.text_typography = Font(family="Poppins", size=12)
        
        # ----------------------------------------------------------------------------------------------------------
        self.label = tk.Label(self.frame, text='Bienvenido de Nuevo', font=self.subtitle_typography, bg='#FFFFFF')
        self.label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # User
        self.label_user = tk.Label(self.frame,text="👤", font=("Arial", 14), bg="white")
        self.label_user.grid(row=1, column=0, padx=5, pady=5)
        self.entry_user = tk.Entry(self.frame, width=25, font=self.text_typography)
        self.entry_user.grid(row=1, column=1, pady=5)
        
        # Password
        self.label_password = tk.Label(self.frame, text="🔒", font=("Arial", 14), bg="white")
        self.label_password.grid(row=2, column=0, padx=5, pady=5)
        self.entry_password = tk.Entry(self.frame, width=25, font=self.text_typography, show="*")
        self.entry_password.grid(row=2, column=1, pady=5)
        
        # ----------------------------------------------------------------------------------------------------------
        btn_enter = tk.Button(self.frame, text="Entrar", font=self.enter_button, bg="#00bf63", fg="black", width=15, command=self.enter)
        btn_enter.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.functions = Functions()
        
    # Funcion para ingresar al sistema
    def enter(self):
        username = self.entry_user.get()
        password = self.entry_password.get()
        if self.functions.Enter(username, password):
            self.root.destroy()
            self.open_menu()
    
    # Funcion para abrir la ventana del menu
    def open_menu(self):
        from src.menu import Menu  # Importar aquí para evitar el bucle
        new_window = tk.Tk()
        app = Menu(new_window)
        new_window.mainloop()
