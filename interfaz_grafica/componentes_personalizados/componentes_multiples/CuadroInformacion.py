from customtkinter import *
from PIL import Image, ImageTk
from tkinter import Label


class cuadroInformacion(CTkFrame):

    def __init__(self, master, imagen, titulo, valor):
        super().__init__(master=master)

        self.configure(width=132, height=121, border_width=2, border_color="#6053AF", fg_color="#FFFFFF")

        self.frameInterno = CTkFrame(self, width=74, height=61, fg_color="#8E8ADB")
        self.frameInterno.place(x=28,y=12)

        self.titulo = CTkLabel(self, width=128, height=15, font=("Arial", 12, "bold"),
                               text_color="#4E458E", text=f"{titulo}")
        self.titulo.place(x=2, y=80)

        self.valor = CTkLabel(self, width=128, height=15, font=("Arial", 12, "bold"),
                               text_color="#000000", text=f"{valor}")
        self.valor.place(x=2, y=97)

        self.imagen = self.redimensionar_imagen(imagen, 52,52)
        self.mostrar_imagen = Label(self.frameInterno,bg="#8E8ADB", image=self.imagen)
        self.mostrar_imagen.place(x=10, y=2)

    def redimensionar_imagen(self, imagen, nuevo_ancho, nuevo_alto):
        imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)
        return ImageTk.PhotoImage(imagen_redimensionada)

    def cambiar_valor(self, texto):
        self.valor.configure(text=f"{texto}")

