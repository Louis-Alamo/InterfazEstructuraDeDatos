from customtkinter import CTkButton,CTkOptionMenu, CTkLabel
from tkinter import Frame, StringVar

class MenuConBoton(Frame):

    def __init__(self, master, lista_opciones,nombre_funcion_boton, variable):
        super().__init__(master=master)
        self.variable = StringVar()
        self.variable.set(variable)  # establece el valor inicial
        self.config( width=602, height=77, bg="#FFFFFF")

        self.titulo = CTkLabel(self, text="Eliga la opcion", font=("Inter", 16, "bold"), text_color="#4E458E")
        self.titulo.place(x=0, y=0)

        self.menu = CTkOptionMenu(master=self, values=lista_opciones, width=390, height=44, font=("Arial",15, "bold")
        ,text_color = "#4E458E", fg_color = "#FFFFFF", button_color = "#FFFFFF",
        dropdown_fg_color = "#FFFFFF", dropdown_text_color = "#4E458E", dropdown_font = ("Arial", 15, "bold"),variable=self.variable
        )
        self.menu.place(x=0, y=33)

        self.boton = CTkButton(master=self,width=124, height=44,text="Aceptar", font=("Arial", 16,"bold"), text_color="#4E458E",
                       border_color="#4E458E", fg_color="#E6E9F9", border_width=2, corner_radius=10, bg_color="#FFFFFF",
                       command=nombre_funcion_boton, hover_color="#d1d6f4", hover=True)
        self.boton.place(x=478,y=33)


    def getSeleccion(self):
        return self.variable.get()
