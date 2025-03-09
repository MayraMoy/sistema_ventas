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
        self.root.geometry('1200x600')
        self.root.configure(bg='#FFFFFF')
        
        # Configuracion de la tipografia
        self.tipografia_subtitulo = Font(family="Poppins", size=20)
        self.tipografia_texto = Font(family="Poppins", size=12)
        
        # --------------------------------------------------------------------------------------------------------------------------------
        self.texto = tk.Label(self.root, text='Bienvenido. Elija una opción.', font=self.tipografia_subtitulo, fg='#000000', bg='#FFFFFF')
        self.texto.pack(pady=10)
        
        # Menu Inicio
        self.menubar = tk.Menu(self.root)
        self.menu_inicio = tk.Menu(self.menubar, tearoff=0)
        self.menu_inicio.add_command(label="Salir", command=self.salir)
        
        # Menu Opciones
        self.menubar = tk.Menu(self.root)
        self.menu_archivo = tk.Menu(self.menubar, tearoff=0)
        self.menu_archivo.add_command(label="Ventas", command=self.realizar_venta)
        self.menu_archivo.add_command(label="Inventario", command=self.ver_inventario)
        self.menu_archivo.add_command(label="Caja", command=self.abrir_caja)
        self.menu_archivo.add_command(label="Reportes", command=self.ver_reportes)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Ajustes", command=self.abrir_ajustes)
        
        self.menubar.add_cascade(label="Inicio", menu=self.menu_inicio)
        self.menubar.add_cascade(label="Opciones", menu=self.menu_archivo)
        
        self.root.config(menu=self.menubar)
        
        # Tamaño de los frames
        frame_width = 210
        frame_height = 210
        
        # Frame Ventas
        self.frame_ventas = tk.Frame(self.root, width=frame_width, height=frame_height, bg='#FFFFFF', border=1, relief='solid')
        self.frame_ventas.place(relx=0.30, rely=0.35, anchor="center")
        self.frame_ventas.propagate(False)
        
        self.icono_ventas = tk.Label(self.frame_ventas, text='🛒', font=("Arial", 60), bg="white")
        self.icono_ventas.pack(pady=20, expand=True)
        
        self.label_ventas = tk.Button(self.frame_ventas, text='Realizar una venta', font=self.tipografia_texto, bg='#FFFFFF', relief='flat', command=self.realizar_venta)
        self.label_ventas.pack(side='bottom', pady=10)
        
        # Frame Inventario
        self.frame_inventario = tk.Frame(self.root, width=frame_width, height=frame_height, bg='#FFFFFF', border=1, relief='solid')
        self.frame_inventario.place(relx=0.50, rely=0.35, anchor="center")
        self.frame_inventario.propagate(False)
        
        self.icono_inventario = tk.Label(self.frame_inventario, text='📦', font=("Arial", 60), bg="white")
        self.icono_inventario.pack(pady=20, expand=True)
        
        self.label_inventario = tk.Button(self.frame_inventario, text='Ver inventario', font=self.tipografia_texto, bg='#FFFFFF', relief='flat', command=self.ver_inventario)
        self.label_inventario.pack(side='bottom', pady=10)
        
        # Frame Caja
        self.frame_caja = tk.Frame(self.root, width=frame_width, height=frame_height, bg='#FFFFFF', border=1, relief='solid')
        self.frame_caja.place(relx=0.70, rely=0.35, anchor="center")
        self.frame_caja.propagate(False)
        
        self.icono_caja = tk.Label(self.frame_caja, text='💰', font=("Arial", 60), bg="white")
        self.icono_caja.pack(pady=20, expand=True)
        
        self.label_caja = tk.Button(self.frame_caja, text='Caja', font=self.tipografia_texto, bg='#FFFFFF', relief='flat', command=self.abrir_caja)
        self.label_caja.pack(side='bottom', pady=10)
        
        # Frame Reportes
        self.frame_reportes = tk.Frame(self.root, width=frame_width, height=frame_height, bg='#FFFFFF', border=1, relief='solid')
        self.frame_reportes.place(relx=0.40, rely=0.75, anchor="center") 
        self.frame_reportes.propagate(False)
        
        self.icono_reportes = tk.Label(self.frame_reportes, text='📄', font=("Arial", 60), bg="white",)
        self.icono_reportes.pack(pady=20, expand=True)
        
        self.label_reportes = tk.Button(self.frame_reportes, text='Reportes', font=self.tipografia_texto, bg='#FFFFFF', relief='flat', command=self.ver_reportes)
        self.label_reportes.pack(side='bottom', pady=10)
        
        # Frame Ajustes
        self.frame_ajustes = tk.Frame(self.root, width=frame_width, height=frame_height, bg='#FFFFFF', border=1, relief='solid')
        self.frame_ajustes.place(relx=0.60, rely=0.75, anchor="center")
        self.frame_ajustes.propagate(False)
        
        self.icono_ajustes = tk.Label(self.frame_ajustes, text='⚙️', font=("Arial", 60), bg="white")
        self.icono_ajustes.pack(pady=20, expand=True)
        
        self.label_ajustes = tk.Button(self.frame_ajustes, text='Ajustes', font=self.tipografia_texto, bg='#FFFFFF', relief='flat', command=self.abrir_ajustes)
        self.label_ajustes.pack(side='bottom', pady=10)
    
    def salir(self):
        self.root.destroy()
    
    def realizar_venta(self):
        self.root.destroy()
        nueva_ventana = tk.Tk()
        app = Venta(nueva_ventana, self.abrir_menu)
        nueva_ventana.mainloop()
    
    def ver_inventario(self):
        self.root.destroy()
        nueva_ventana = tk.Tk()
        app = Inventario(nueva_ventana, self.abrir_menu)
        nueva_ventana.mainloop()
    
    def abrir_caja(self):
        self.root.destroy()
        nueva_ventana = tk.Tk()
        app = Caja(nueva_ventana, self.abrir_menu)
        nueva_ventana.mainloop()
    
    def ver_reportes(self):
        self.root.destroy()
        nueva_ventana = tk.Tk()
        app = Reportes(nueva_ventana, self.abrir_menu)
        nueva_ventana.mainloop()
    
    def abrir_ajustes(self):
        self.root.destroy()
        nueva_ventana = tk.Tk()
        app = Ajustes(nueva_ventana, self.abrir_menu)
        nueva_ventana.mainloop()
    
    def abrir_menu(self):
        nueva_ventana = tk.Tk()
        app = Menu(nueva_ventana)
        nueva_ventana.mainloop()