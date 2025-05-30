import tkinter as tk
from tkinter.font import Font

class VentanaInventario:
    def __init__(self, root):
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
        
        # Configuracion de la tipografia
        self.subtitle_typography = Font(family="Poppins", size=20)
        self.text_typography = Font(family="Poppins", size=12)
        
        # --------------------------------------------------------------------------------------------------------------------------------
        
        self.label_welcome = tk.Label(root, text="Bienvenido de nuevo.", font=self.subtitle_typography, bg='white')
        self.label_welcome.pack(pady=10)
        
        self.frame_sales = tk.Frame(self.root, padx=10, pady=10, relief="solid", borderwidth=1, bg='white')
        self.frame_sales.pack(pady=10, padx=15, fill="x")
        
        self.entry_search_engine = tk.Entry(self.frame_sales, width=20, font=self.text_typography, relief='solid')
        self.entry_search_engine.grid(row=1, column=1, pady=5, padx=10)
        
        # Menu
        self.menubar = tk.Menu(self.root)
        self.menu_inicio = tk.Menu(self.menubar, tearoff=0)
        self.menu_inicio.add_command(label="Salir", command=self.salir)
        self.menu_inicio.add_command(label="Volver", command=self.volver)
        
        self.menubar.add_cascade(label="Opciones", menu=self.menu_inicio)
        
        self.root.config(menu=self.menubar)
        
        # Frame buscador
        
        
    def salir(self):
        self.root.destroy()
    
    def volver(self):
        self.root.destroy()
        
# Ejecutar la aplicación
root = tk.Tk()
app = VentanaInventario(root)
root.mainloop()
