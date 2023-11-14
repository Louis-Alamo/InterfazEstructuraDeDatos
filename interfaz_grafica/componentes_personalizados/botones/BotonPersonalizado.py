from customtkinter import CTkButton, CTk

class BotonPersonalizado(CTkButton):
    def __init__(self, master, funcion_boton, nombre_boton):
        super().__init__(master=master)
        self.configure(width=124, height=44,text=f"{nombre_boton}", font=("Arial", 16,"bold"), text_color="#4E458E",
                       border_color="#4E458E", fg_color="#E6E9F9", border_width=2, corner_radius=10, bg_color="#FFFFFF",
                       command=funcion_boton, hover_color="#d1d6f4", hover=True)


