from customtkinter import CTkButton
class BotonPersonalizado(CTkButton):

    def __init__(self, nombre_funcion, nombre_boton):
        self.configure(self,width=124, height=44,text=f"{nombre_boton}", font=("Arial", 16,"bold"), text_color="#4E458E",
                       border_color="#4E458E", fg_color="#E6E9F9", border_width=2, corner_radius=10, bg_color="#FFFFFF",
                       command=nombre_funcion, hover_color="#d1d6f4", hover=True)


