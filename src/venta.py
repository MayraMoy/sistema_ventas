import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

class Venta:
    def __init__(self, root, abrir_menu_callback):
        self.root = root
        self.root.title('Sistema de Gestion de Ventas')

        # ------------------------------------------------------------------------
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 1200
        window_height = 600                                # Centra la ventana en la pantalla

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}") # Centrada
        self.root.configure(bg='#FFFFFF')
        
        # ------------------------------------------------------------------------
        self.abrir_menu_callback = abrir_menu_callback
        
        # Configuracion de la tipografia
        self.subtitle_typography = Font(family="Poppins", size=20)
        self.text_typography = Font(family="Poppins", size=12)
        
        # --------------------------------------------------------------------------------------------------------------------------------
        self.label_welcome = tk.Label(root, text="Bienvenido, complete el formulario.", font=self.subtitle_typography, bg='white')
        self.label_welcome.pack(pady=10)
        
        self.frame_sales = tk.Frame(self.root, padx=10, pady=10, relief="solid", borderwidth=1, bg='white')
        self.frame_sales.pack(pady=10, padx=15, fill="x")

        self.label_code = tk.Label(self.frame_sales, text=" Codigo ", font=self.text_typography, bg="#00bf63")
        self.label_code.grid(row=1, column=0, padx=5, pady=5)
        self.entry_code = tk.Entry(self.frame_sales, width=10, font=self.text_typography, relief='solid')
        self.entry_code.grid(row=1, column=1, pady=5, padx=10)
        
        self.label_description = tk.Label(self.frame_sales, text=" Descripcion ", font=self.text_typography, bg="#00bf63")
        self.label_description.grid(row=1, column=2, padx=5, pady=5)
        self.entry_description = tk.Entry(self.frame_sales, width=20, font=self.text_typography, relief='solid')
        self.entry_description.grid(row=1, column=3, pady=5, padx=10)      
        
        self.label_price = tk.Label(self.frame_sales, text=" Precio ", font=self.text_typography, bg="#00bf63")
        self.label_price.grid(row=1, column=4, padx=5, pady=5)
        self.entry_price = tk.Entry(self.frame_sales, width=10, font=self.text_typography, relief='solid')
        self.entry_price.grid(row=1, column=5, pady=5, padx=10)   
        
        self.label_unit = tk.Label(self.frame_sales, text=" Unidad ", font=self.text_typography, bg="#00bf63")
        self.label_unit.grid(row=2, column=0, padx=5, pady=5)
        self.entry_unit = tk.Entry(self.frame_sales, width=10, font=self.text_typography, relief='solid')
        self.entry_unit.grid(row=2, column=1, pady=5, padx=10) 
        
        self.label_total = tk.Label(self.frame_sales, text=" Total ", font=self.text_typography, bg="#00bf63")
        self.label_total.grid(row=2, column=2, padx=5, pady=5)
        self.entry_total = tk.Entry(self.frame_sales, width=20, font=self.text_typography, relief='solid')
        self.entry_total.grid(row=2, column=3, pady=5, padx=10) 
        
        self.label_further = tk.Button(self.frame_sales, text=" + ", font=self.text_typography, bg="#00bf63")
        self.label_further.grid(row=2, column=4, padx=5, pady=5)
        
        self.board = ttk.Treeview(self.root, columns=('Codigo', 'Descripcion', 'Precio', 'Unidad', 'Total'))
        self.board.heading("Codigo", text="Código")
        self.board.heading("Descripcion", text="Descripción")
        self.board.heading("Precio", text="Precio")
        self.board.heading("Unidad", text="Unidad")
        self.board.heading("Total", text="Total")
        self.board.pack(pady=10, padx=15, fill="both", expand=True)
        
        self.frame_total = tk.Frame(self.root, bg="#FFFFFF")
        self.frame_total.pack(pady=5)

        self.total_finals = tk.Label(self.frame_total, text="Total Final:", bg="#00bf63", fg="white", font=self.text_typography)
        self.total_finals.pack(side="left", padx=5)
        self.total_finals_label = tk.Label(self.frame_total, text="$0.00", font=self.text_typography, bg="#FFFFFF")
        self.total_finals_label.pack(side="left", pady=10)
        
        self.menubar = tk.Menu(self.root)
        self.menu_inicio = tk.Menu(self.menubar, tearoff=0)
        self.menu_inicio.add_command(label="Salir", command=self.salir)
        self.menu_inicio.add_command(label="Volver", command=self.volver)
        
        self.menubar.add_cascade(label="Opciones", menu=self.menu_inicio)
        
        self.root.config(menu=self.menubar)
        
        # ----------------------------------------------------------------------------------------------------------------------------
        
        
        
    def salir(self):
        self.root.destroy()
    
    def volver(self):
        self.root.destroy()
        self.abrir_menu_callback()