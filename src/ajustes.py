import tkinter as tk
from tkinter.font import Font

class Ajustes:
    def __init__(self, root, abrir_menu_callback):
        self.root = root
        self.root.title('Sistema de Gestion de Ventas')
        
        # ------------------------------------------------------------------------
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 1200
        window_height = 600                               # Centra la ventana en la pantalla

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}") # Centrada
        self.root.configure(bg='#FFFFFF')
        
        # ------------------------------------------------------------------------
        self.abrir_menu_callback = abrir_menu_callback
        
        # Configuracion de la tipografia
        self.tipografia_subtitulo = Font(family="Poppins", size=20)
        self.tipografia_texto = Font(family="Poppins", size=12)
        
        # --------------------------------------------------------------------------------------------------------------------------------
        self.texto = tk.Label(self.root, text='Bienvenido, complete el formulario.', font=self.tipografia_subtitulo, fg='#000000', bg='#FFFFFF')
        self.texto.pack(pady=10)
        
        self.menubar = tk.Menu(self.root)
        self.menu_inicio = tk.Menu(self.menubar, tearoff=0)
        self.menu_inicio.add_command(label="Salir", command=self.salir)
        self.menu_inicio.add_command(label="Volver", command=self.volver)
        
        self.menubar.add_cascade(label="Opciones", menu=self.menu_inicio)
        
        self.root.config(menu=self.menubar)
    
    def salir(self):
        self.root.destroy()
    
    def volver(self):
        self.root.destroy()
        self.abrir_menu_callback()