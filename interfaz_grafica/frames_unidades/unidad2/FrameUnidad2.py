from interfaz_grafica.componentes_personalizados.frames.FramePersonalizado import FramePersonalizado
from interfaz_grafica.componentes_personalizados.componentes_multiples.Componente import Componente
from interfaz_grafica.frames_unidades.unidad2.euclides.FrameEuclides import FrameEuclides
from interfaz_grafica.frames_unidades.unidad2.factorial.FrameFactorial import FrameFactorial
from interfaz_grafica.frames_unidades.unidad2.fibonaci.FrameFibonaci import FrameFibonaci
from interfaz_grafica.frames_unidades.unidad2.imprimir_arreglo_derecha_izquierda.FrameImprimirArregloDerechaIzquierda import FrameArregloDerechaIzquierda
from interfaz_grafica.frames_unidades.unidad2.imprimir_arreglo_izquierda_derecha.FrameImprimirArregloIzquierdaDerecha import FrameArregloIzqueirdaDerecha
from interfaz_grafica.frames_unidades.unidad2.suma_arreglo.FrameSumaArreglo import FrameSumaArreglo
from interfaz_grafica.frames_unidades.unidad2.torres_de_hanoi.FrameTorresHanoi import FrameTorresDeHanoi
class FrameUnidad2(FramePersonalizado):

    def __init__(self, master):
        super().__init__(master=master)
        self.frame = None
        self.editar_titulo("Unidad 2 Recursividad")

        self.factorial_boton = Componente("Factorial","Descripcion",master=self.canvas, funcion_nombre=self.factorial_funcion)
        self.lista_componentes.append(self.factorial_boton)

        self.fibonaci_boton = Componente("Fibonaci", "Descripcion",master=self.canvas, funcion_nombre=self.fibonaci_funcion)
        self.lista_componentes.append(self.fibonaci_boton)

        self.imprimir_arreglo_derecha_izquierda_boton = Componente("Imprimir arreglo der-izq", "Descripcion",master=self.canvas, funcion_nombre=self.imprimir_arreglo_derecha_izquierda_funcion)
        self.lista_componentes.append(self.imprimir_arreglo_derecha_izquierda_boton)

        self.imprimir_arreglo_izquierda_derecha_boton = Componente("Imprimir arreglo izq-der", "Descripcion",master=self.canvas, funcion_nombre=self.imprimir_arreglo_izquierda_derecha_funcion)
        self.lista_componentes.append(self.imprimir_arreglo_izquierda_derecha_boton)

        self.suma_arreglo_boton = Componente("Suma de un arreglo", "Suma los datos contenidos de un arreglo",master=self.canvas, funcion_nombre=self.suma_de_un_arreglo_funcion)
        self.lista_componentes.append(self.suma_arreglo_boton)

        self.torres_de_hanoi_boton = Componente("Torres de hanoi", "Algoritmo que indica los pasos a resolver del juego de torres de hanoi",master=self.canvas, funcion_nombre=self.torres_de_hanoi_funcion)
        self.lista_componentes.append(self.torres_de_hanoi_boton)

        self.euclides_boton = Componente("Euclides", "Descripcion",master=self.canvas, funcion_nombre=self.euclides_funcion)
        self.lista_componentes.append(self.euclides_boton)

        self.agregar_lista_componentes(self.lista_componentes)


    def fibonaci_funcion(self):
        self.frame = FrameFibonaci(master=self, titulo="Fibonaci")
        self.frame.place(x=0, y=0)

    def euclides_funcion(self):
        self.frame = FrameEuclides(master=self, titulo="Euclides")
        self.frame.place(x=0, y=0)
    def factorial_funcion(self):
        self.frame = FrameFactorial(master=self, titulo="Factorial")
        self.frame.place(x=0, y=0)

    def imprimir_arreglo_derecha_izquierda_funcion(self):
        self.frame = FrameArregloDerechaIzquierda(master=self, titulo="Imprimir derecha-izquierda")
        self.frame.place(x=0, y=0)

    def imprimir_arreglo_izquierda_derecha_funcion(self):
        self.frame = FrameArregloIzqueirdaDerecha(master=self, titulo="Imprimir izquierda-derecha")
        self.frame.place(x=0, y=0)


    def suma_de_un_arreglo_funcion(self):
        self.frame = FrameSumaArreglo(master=self, titulo="Suma de un arreglo")
        self.frame.place(x=0, y=0)

    def torres_de_hanoi_funcion(self):
        self.frame = FrameTorresDeHanoi(master=self, titulo="Torres de hanoi")
        self.frame.place(x=0, y=0)


