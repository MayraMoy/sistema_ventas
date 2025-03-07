from PIL import ImageTk,Image

def leer_imagen( path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.Resampling.LANCZOS))

def centrar_ventana(ventana, ancho_ventana, largo_ventana):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()
    
    x = int((pantalla_ancho/3) - (ancho_ventana/3))
    y = int((pantalla_largo/2) - (largo_ventana/2))
    
    return ventana.geometry(f"{ancho_ventana}x{largo_ventana}+{x}+{y}")