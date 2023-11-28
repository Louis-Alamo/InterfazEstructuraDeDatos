from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConBoton import CampoConBoton
from interfaz_grafica.frames_unidades.unidad3.listas.Nodo import Nodo
from interfaz_grafica.frames_unidades.unidad6.busqueda_secuencial.desordenado.BusquedaSecuencialDesordenado import BusquedaSecuencialDesordenado
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from tkinter import Frame, simpledialog, messagebox
class FrameSecuencialListas(FramePersonalizadoExtra):

    def __init__(self, master, titulo):
        super().__init__(master=master, titulo=titulo)
        self.seleccion = "iterativo"
        self.separacion = 100
        self.bandera_creacion = False
        self.nodo = Nodo()
        self.mensajero = BusquedaSecuencialDesordenado()

        self.iterativo_boton = BotonSeleccionManera(master=self, nombre_boton="iterativo",nombre_funcion=self.seleccion_iterativo)
        self.iterativo_boton.place(x=39, y=75)

        self.recursivo_boton = BotonSeleccionManera(master=self, nombre_boton="recursivo", nombre_funcion=self.seleccion_recursivo)
        self.recursivo_boton.place(x=189, y=75)

        self.campo = CampoConBoton(master=self.canvas, titulo="Ingrese los valores del arreglo", nombre_boton="Agregar", nombre_funcion=self.obtener_datos)
        self.lista_componentes.append(self.campo)

        self.linea = Frame(master=self.canvas,  width=663,height=3, bg="#4E458E")
        self.lista_componentes.append(self.linea)

        self.campo2  = CampoConBoton(master=self.canvas, titulo="Ingrese el valor a buscar", nombre_boton="Buscar", nombre_funcion=self.opcion_seleccionada)
        self.lista_componentes.append(self.campo2)

        self.area_texto = AreaDeInformacion(master=self.canvas, titulo="Resultado")
        self.lista_componentes.append(self.area_texto)


        self.agregar_lista_componentes(self.lista_componentes)




        self.seleccion_iterativo()

    def seleccion_iterativo(self):
        self.seleccion = "iterativo"
        self.iterativo_boton.seleccionado()
        self.recursivo_boton.deseleccionado()

    def seleccion_recursivo(self):
        self.seleccion = "recursivo"
        self.recursivo_boton.seleccionado()
        self.iterativo_boton.deseleccionado()


    def obtener_datos(self):
        pass


    def iterativo(self):
        pass

    def recursivo(self):
        pass

    def opcion_seleccionada(self):
        if self.seleccion == "iterativo":
            self.iterativo()
        elif self.seleccion == "recursivo":
            self.recursivo()