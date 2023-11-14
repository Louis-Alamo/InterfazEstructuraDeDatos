from customtkinter import CTkButton
from tkinter import Frame


class BotonUnidad(Frame):

    def __init__(self, master, nombre_boton, nombre_funcion):
        super().__init__(master=master)


        self.config(width=193, height=37, bg="#6053AF")

        self.linea = Frame(self, width=5, height=37, bg="#FFFFFF")
        self.linea.pack(side="left")

        self.boton = CTkButton(master=self, width=186,border_width=0, border_color="#6053AF",
                               height=37,font=("Inter", 15),text_color="#D1D6F4",hover=False,fg_color="#6053AF",corner_radius=0,
                               text=f"{nombre_boton}", command=nombre_funcion)
        self.boton.pack(side="right")


        self.linea.pack_forget()





    def seleccionado(self):
        self.boton.configure(text_color="#FFFFFF", font=("Inter", 18, "bold"))
        self.linea.pack(side="left")


    def deseleccionado(self):
        self.boton.configure(text_color="#9799E2",font=("Inter", 16))
        self.linea.pack_forget()



