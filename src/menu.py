import tkinter as tk
from tkinter.font import Font
from src.venta import Venta
from src.inventario import Inventario
from src.caja import Caja
from src.reportes import Reportes
from src.ajustes import Ajustes

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title('Sistema de Gestion de Ventas')
        
        # ------------------------------------------------------------------------
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 1200
        window_height = 600                           # Centra la ventana en la pantalla

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}") 
        self.root.configure(bg='#FFFFFF')
        
        # Configuracion de la tipografia
        self.subtitle_typography = Font(family="Poppins", size=20)
        self.text_typography = Font(family="Poppins", size=12)
        
        # --------------------------------------------------------------------------------------------------------------------------------
        self.text = tk.Label(self.root, text='Bienvenido. Elija una opción.', font=self.subtitle_typography, fg='#000000', bg='#FFFFFF')
        self.text.pack(pady=10)
        
        # Menu Inicio
        self.menubar = tk.Menu(self.root)
        self.start_menu = tk.Menu(self.menubar, tearoff=0)
        self.start_menu.add_command(label="Salir", command=self.go_out)
        
        # Menu Opciones
        self.menubar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Ventas", command=self.make_sale)
        self.file_menu.add_command(label="Inventario", command=self.see_inventory)
        self.file_menu.add_command(label="Caja", command=self.open_box)
        self.file_menu.add_command(label="Reportes", command=self.see_reports)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Ajustes", command=self.open_settings)
        
        self.menubar.add_cascade(label="Inicio", menu=self.start_menu)
        self.menubar.add_cascade(label="Opciones", menu=self.file_menu)
        
        self.root.config(menu=self.menubar)
        
        # Tamaño de los frames
        frame_width = 210
        frame_height = 210
        
        # Frame Ventas
        self.frame_sales = tk.Frame(self.root, width=frame_width, height=frame_height, bg='#FFFFFF', border=1, relief='solid')
        self.frame_sales.place(relx=0.30, rely=0.35, anchor="center")
        self.frame_sales.propagate(False)
        
        self.sales_icon = tk.Label(self.frame_sales, text='🛒', font=("Arial", 60), bg="white")
        self.sales_icon.pack(pady=20, expand=True)
        
        self.label_sales = tk.Button(self.frame_sales, text='Realizar una venta', font=self.text_typography, bg='#FFFFFF', relief='flat', command=self.make_sale)
        self.label_sales.pack(side='bottom', pady=10)
        
        # Frame Inventario
        self.frame_inventory = tk.Frame(self.root, width=frame_width, height=frame_height, bg='#FFFFFF', border=1, relief='solid')
        self.frame_inventory.place(relx=0.50, rely=0.35, anchor="center")
        self.frame_inventory.propagate(False)
        
        self.inventory_icon = tk.Label(self.frame_inventory, text='📦', font=("Arial", 60), bg="white")
        self.inventory_icon.pack(pady=20, expand=True)
        
        self.label_inventory = tk.Button(self.frame_inventory, text='Ver inventario', font=self.text_typography, bg='#FFFFFF', relief='flat', command=self.see_inventory)
        self.label_inventory.pack(side='bottom', pady=10)
        
        # Frame Caja
        self.frame_box = tk.Frame(self.root, width=frame_width, height=frame_height, bg='#FFFFFF', border=1, relief='solid')
        self.frame_box.place(relx=0.70, rely=0.35, anchor="center")
        self.frame_box.propagate(False)
        
        self.box_icon = tk.Label(self.frame_box, text='💰', font=("Arial", 60), bg="white")
        self.box_icon.pack(pady=20, expand=True)
        
        self.label_box = tk.Button(self.frame_box, text='Caja', font=self.text_typography, bg='#FFFFFF', relief='flat', command=self.open_box)
        self.label_box.pack(side='bottom', pady=10)
        
        # Frame Reportes
        self.frame_reports = tk.Frame(self.root, width=frame_width, height=frame_height, bg='#FFFFFF', border=1, relief='solid')
        self.frame_reports.place(relx=0.40, rely=0.75, anchor="center") 
        self.frame_reports.propagate(False)
        
        self.reports_icono = tk.Label(self.frame_reports, text='📄', font=("Arial", 60), bg="white",)
        self.reports_icono.pack(pady=20, expand=True)
        
        self.label_reports = tk.Button(self.frame_reports, text='Reportes', font=self.text_typography, bg='#FFFFFF', relief='flat', command=self.see_reports)
        self.label_reports.pack(side='bottom', pady=10)
        
        # Frame Ajustes
        self.frame_settings = tk.Frame(self.root, width=frame_width, height=frame_height, bg='#FFFFFF', border=1, relief='solid')
        self.frame_settings.place(relx=0.60, rely=0.75, anchor="center")
        self.frame_settings.propagate(False)
        
        self.settings_icon = tk.Label(self.frame_settings, text='⚙️', font=("Arial", 60), bg="white")
        self.settings_icon.pack(pady=20, expand=True)
        
        self.label_settings = tk.Button(self.frame_settings, text='Ajustes', font=self.text_typography, bg='#FFFFFF', relief='flat', command=self.open_settings)
        self.label_settings.pack(side='bottom', pady=10)
    
    def go_out(self):
        self.root.destroy()
    
    def make_sale(self):
        self.root.destroy()
        new_window = tk.Tk()
        app = Venta(new_window, self.open_menu)
        new_window.mainloop()
    
    def see_inventory(self):
        self.root.destroy()
        new_window = tk.Tk()
        app = Inventario(new_window, self.open_menu)
        new_window.mainloop()
    
    def open_box(self):
        self.root.destroy()
        new_window = tk.Tk()
        app = Caja(new_window, self.open_menu)
        new_window.mainloop()
    
    def see_reports(self):
        self.root.destroy()
        new_window = tk.Tk()
        app = Reportes(new_window, self.open_menu)
        new_window.mainloop()
    
    def open_settings(self):
        self.root.destroy()
        new_window = tk.Tk()
        app = Ajustes(new_window, self.open_menu)
        new_window.mainloop()
    
    def open_menu(self):
        new_window = tk.Tk()
        app = Menu(new_window)
        new_window.mainloop()