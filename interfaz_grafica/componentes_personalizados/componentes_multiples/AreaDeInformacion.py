from tkinter import Frame, Tk
from customtkinter import CTkTextbox, CTkLabel, CTkScrollbar, END

class AreaDeInformacion(Frame):

    def __init__(self, master, titulo):
        super().__init__(master=master)

        self.config(width=602, height=107, bg="#FFFFFF")

        self.titulo = CTkLabel(self, text=f"{titulo}", font=("Inter", 16, "bold"), text_color="#4E458E")
        self.titulo.place(x=0, y=0)

        self.area_texto = CTkTextbox(self, width=602,font=("Arial",15), height=76,fg_color="#f1f3fc", border_width=2,
                                     border_color="#4E458E")
        self.area_texto.place(x=0,y=31)
        self.area_texto.configure(state="disable")

        # Crear la barra de desplazamiento
        self.scrollbar = CTkScrollbar(self, command=self.area_texto.yview,hover=False,button_color="#4E458E",fg_color="#f1f3fc", height=70)  # Pasar 'height' al constructor
        self.scrollbar.place(x=582, y=33)

        # Conectar el evento de desplazamiento del área de texto a la barra de desplazamiento
        self.area_texto.configure(yscrollcommand=self.scrollbar.set)

    def mostrar_informacion_estructura_numerica(self, informacion):
        # Filtrar los ceros y convertir los enteros a cadenas antes de mostrarlos
        elementos_validos = filter(lambda x: x != 0, informacion)
        texto_a_mostrar = "→".join(map(str, elementos_validos))

        # Habilitar el área de texto, configurar el texto y deshabilitarla nuevamente
        self.area_texto.configure(state="normal")
        self.area_texto.delete(1.0, END)  # Borrar contenido existente
        self.area_texto.insert(1.0, texto_a_mostrar)
        self.area_texto.configure(state="disable")

    def mostrar_texto_individual(self, informacion):
        self.limpiar_area()
        self.area_texto.configure(state="normal")
        self.area_texto.insert(1.0,str(informacion))
        self.area_texto.configure(state="disable")

    def mostrar_texto_concatenado(self, texto):
        self.area_texto.configure(state="normal")
        self.area_texto.insert(1.0,str(texto))
        self.area_texto.configure(state="disable")

    def limpiar_area(self):
        self.area_texto.configure(state="normal")
        self.area_texto.delete(1.0, END)
        self.area_texto.configure(state="disable")




