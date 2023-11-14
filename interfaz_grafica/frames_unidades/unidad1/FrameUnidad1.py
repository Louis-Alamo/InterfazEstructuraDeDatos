from interfaz_grafica.componentes_personalizados.frames.FramePersonalizado import FramePersonalizado
from interfaz_grafica.componentes_personalizados.componentes_multiples.Componente import Componente
from interfaz_grafica.frames_unidades.unidad1.FrameMuchasVaraibles import FrameMuchasVaraibles
from interfaz_grafica.frames_unidades.unidad1.FrameDobleLectura import FrameDobleLectura
from interfaz_grafica.frames_unidades.unidad1.FrameConArreglos import FrameArreglos

class FrameUnidad1(FramePersonalizado):

    def __init__(self, master):
        super().__init__(master=master)

        self.editar_titulo("Unidad 1 Tipo de datos")
        self.frame = None


        # Agregar el primer componente
        self.calificaciones_arreglos = Componente("Con arreglos",
                                                  "Toma la cantidad de valores dados por el usuario y los guarda en un arreglo",
                                                  master=self.canvas, funcion_nombre=self.calificaciones_arreglo_funcion)
        self.lista_componentes.append(self.calificaciones_arreglos)
        # Agregar el segundo componente debajo del primero
        self.calificaciones_doble_lectura = Componente("Doble lectura",
                                                   "Pide al usuario dos veces los datos para \npoder procesarlos ",
                                                       master=self.canvas, funcion_nombre=self.calificaciones_doble_lectura_funcion)
        self.lista_componentes.append(self.calificaciones_doble_lectura)

        # Agregar el tercer componente debajo del segundo
        self.calificaciones_muchas_variables = Componente("Muchas variables",
                                                   "Utiliza mucahs variables para guardar los \ndatos datos por el usuario",
                                                          master=self.canvas, funcion_nombre=self.calificaciones_muchas_variables_funcion)
        self.lista_componentes.append(self.calificaciones_muchas_variables)

        self.agregar_lista_componentes(self.lista_componentes)
    def calificaciones_arreglo_funcion(self):
        self.frame = FrameArreglos(master=self, titulo="Con arreglos")
        self.frame.place(x=0, y=0)

    def calificaciones_doble_lectura_funcion(self):
        self.frame = FrameDobleLectura(master=self, titulo="Doble lectura")
        self.frame.place(x=0, y=0)

    def calificaciones_muchas_variables_funcion(self):
        self.frame = FrameMuchasVaraibles(master=self, titulo="Muchas varaibles")
        self.frame.place(x=0, y=0)




# # Crear la ventana principal
# ventana = Tk()
# ventana.title("Ejemplo de Frame con Imagen")
#
# # Crear una instancia de la clase FrameUnidad1 y empaquetarla en la ventana principal
# frame_unidad1 = FrameUnidad1(master=ventana)
# frame_unidad1.pack()
#
# # Iniciar el bucle principal
# ventana.mainloop()