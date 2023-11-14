from customtkinter import CTkButton
from tkinter import Frame,Tk

class BotonSeleccionManera(Frame):

    def __init__(self, master, nombre_boton, nombre_funcion):
        super().__init__(master=master)

        self.config(width=136, height=40, bg="#FFFFFF")

        self.boton = CTkButton(master=self, width=136, height=40,font=("Inter", 16),hover_color="#f1f3fc",
                               text_color="#9799E2",hover=True,fg_color="#FFFFFF",corner_radius=0,
                               text=f"{nombre_boton}", command=nombre_funcion)
        self.boton.pack()


        self.linea = Frame(self, width=136, height=2, bg="#4E458E")
        self.linea.pack()
        self.linea.pack_forget()


    def seleccionado(self):
        self.boton.configure(text_color="#433d72", font=("Inter", 17, "bold"))
        self.linea.pack()


    def deseleccionado(self):
        self.boton.configure(text_color="#9799E2",font=("Inter", 16))
        self.linea.pack_forget()

