from tkinter import Frame
from customtkinter import *

class CampoConTitulo(Frame):

    def __init__(self, master, titulo):
        super().__init__(master=master)

        self.config(width=602, height=77, bg="#FFFFFF")
        self.titulo = CTkLabel(self, text=f"{titulo}", font=("Inter", 16, "bold"), text_color="#4E458E")
        self.titulo.place(x=0, y=0)

        self.campo = CTkEntry(self,width=390,font=("Arial",15), height=44,fg_color="#f1f3fc", border_width=2,
                                     border_color="#4E458E")
        self.campo.place(x=0, y=33)

    def obtener_datos(self):
        return self.campo.get()

    def limpiar_campo(self):
        self.campo.delete(0, END)