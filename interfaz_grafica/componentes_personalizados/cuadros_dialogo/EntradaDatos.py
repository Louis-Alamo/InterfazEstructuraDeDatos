from customtkinter import *
from interfaz_grafica.componentes_personalizados.componentesSolitarios.BotonPersonalizado import BotonPersonalizado
class EntradaDatos():

    def __init__(self, titulo_ventana, titulo_campo):

        self.ventana_dialogo = CTk()
        self.ventana_dialogo.title(titulo_ventana)
        self.ventana_dialogo.geometry("400x300")






        self.ventana_dialogo.mainloop()


    def obtener_datos(self):
        pass

EntradaDatos("Ingresa datos", "Datos a ingresar")