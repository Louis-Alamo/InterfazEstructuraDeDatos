from tkinter import Frame, Label, Tk, Button
from PIL import Image, ImageTk


class Componente(Frame):
    def __init__(self, titulo, descripcion, master, funcion_nombre):
        super().__init__(master)
        self.config(width=584, height=164, bg="#FFFFFF")

        imagen_fondo = Image.open("../imagenes/componente_fondo.png")
        self.imagen_fondo_redimensionada = self.redimensionar_imagen(imagen_fondo, 584, 164)
        self.etiqueta_fondo = Label(self, image=self.imagen_fondo_redimensionada, bg="#FFFFFF")
        self.etiqueta_fondo.place(x=0, y=0)

        self.titulo = Label(self, text=f"{titulo}", font=("Inter", 18, "bold"), bg="#F1F3FC", fg="#282442")
        self.titulo.place(x=208, y=28)

        self.descripcion = Label(self, text=f"{descripcion}", font=("Inter", 10), bg="#F1F3FC", fg="#8E8ADB",
                                 anchor="w", width=45, wraplength=1000)  # Configura wraplength con un valor grande
        self.descripcion.place(x=208, y=68)

        imagen = Image.open("../imagenes/Arreglo de carpetas.png")
        self.imagen_resimensionada = self.redimensionar_imagen(imagen, 103, 108)
        self.icono = Label(self, image=self.imagen_resimensionada)
        self.icono.place(x=47, y=28)

        imagen_boton = Image.open("../imagenes/icon_boton.png")
        self.imagen_boton_redimensionada = self.redimensionar_imagen(imagen_boton, 47, 47)
        self.boton = Button(self, image=self.imagen_boton_redimensionada, cursor="Hand2", border=0, bg="#F1F3FC",
                            command=funcion_nombre)
        self.boton.place(x=529, y=108)

    def redimensionar_imagen(self, imagen, nuevo_ancho, nuevo_alto):
        imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)
        return ImageTk.PhotoImage(imagen_redimensionada)

    def set_titulo(self):
        pass

    def set_descripcion(self):
        pass

    def set_icono(self):
        pass