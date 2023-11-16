from interfaz_grafica.componentes_personalizados.frames.FramePersonalizado import FramePersonalizado
from interfaz_grafica.componentes_personalizados.componentes_multiples.Componente import Componente
from interfaz_grafica.frames_unidades.unidad5.burbuja.FrameBurbuja import FrameBurbuja
from interfaz_grafica.frames_unidades.unidad5.quick_sort.FrameQuickSort import FrameQuickSort
from interfaz_grafica.frames_unidades.unidad5.shell_sort.FrameShellSort import FrameShellSort
from interfaz_grafica.frames_unidades.unidad5.radix.FrameRadix import FrameRadix
from interfaz_grafica.frames_unidades.unidad5.ordenacion_externa.FrameOrdenacionExterna import FrameOrdenacionExterna



class FrameUnidad5(FramePersonalizado):

    def __init__(self, master):
        super().__init__(master=master)

        super().editar_titulo("Unidad 5 Metodos de ordenamiento")

        #COmponentes de algoritmos de ordenacion interno
        self.burbuja_componente = Componente("Burbuja", "Algoritmo de ordenación simple, compara elementos \nadyacentes y los intercambia si están en el orden\nincorrecto", master=self.canvas, funcion_nombre=self.burbuja_funcion)
        self.lista_componentes.append(self.burbuja_componente)

        self.quickSort_componente = Componente("QuickSort", "Algoritmo de ordenación que se basa en la selección de\nun pivote y la división de la lista en dos subconjuntos", master=self.canvas, funcion_nombre=self.quickSort_funcion)
        self.lista_componentes.append(self.quickSort_componente)

        self.shellSort_componente = Componente("ShellSort", "Mejora el método de inserción al ordenar subgrupos de\nelementos con brechas decrecientes.", master=self.canvas, funcion_nombre=self.shellSort_funcion)
        self.lista_componentes.append(self.shellSort_componente)

        self.radix_componente = Componente("Radix", "Ordena los números procesando sus dígitos de menor a \nmayor o viceversa", master=self.canvas, funcion_nombre=self.radix_funcion)
        self.lista_componentes.append(self.radix_componente)

        self.ordenacion_externa_componente = Componente("Ordenacion", "Ordena los números procesando sus dígitos de menor a \nmayor o viceversa", master=self.canvas, funcion_nombre=self.ordenacion_externa)
        self.lista_componentes.append(self.ordenacion_externa_componente)


        super().agregar_lista_componentes(self.lista_componentes)
    #Algoritmos de ordenamiento interno
    def burbuja_funcion(self):
        self.frame_burbuja = FrameBurbuja(master=self,titulo="Burbuja")
        self.frame_burbuja.place(x=0, y=0)

    def quickSort_funcion(self):
        self.frame_burbuja = FrameQuickSort(master=self,titulo="QuickSort")
        self.frame_burbuja.place(x=0, y=0)

    def shellSort_funcion(self):
        self.frame_burbuja = FrameShellSort(master=self,titulo="ShellSort")
        self.frame_burbuja.place(x=0, y=0)

    def radix_funcion(self):
        self.frame_burbuja = FrameRadix(master=self,titulo="Radix")
        self.frame_burbuja.place(x=0, y=0)

    def ordenacion_externa(self):
        self.frame_burbuja = FrameOrdenacionExterna(master=self,titulo="Ordenacion externa")
        self.frame_burbuja.place(x=0, y=0)



