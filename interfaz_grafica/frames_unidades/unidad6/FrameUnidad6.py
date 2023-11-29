from interfaz_grafica.componentes_personalizados.frames.FramePersonalizado import FramePersonalizado
from interfaz_grafica.componentes_personalizados.componentes_multiples.Componente import Componente
from interfaz_grafica.frames_unidades.unidad3.listas.FrameListas import FrameListas
from interfaz_grafica.frames_unidades.unidad6.busqueda_binaria.FrameBusquedaBinaria import FrameBusquedaBinaria
from interfaz_grafica.frames_unidades.unidad6.busqueda_secuencial.desordenado.FrameSecuencialDesordenado import FrameSecuencialDesordenado
from interfaz_grafica.frames_unidades.unidad6.busqueda_secuencial.ordenado.FrameSecuencialOrdenado import FrameSecuencialOrdenado
from interfaz_grafica.frames_unidades.unidad6.busqueda_funciones_hash.FrameBusquedaFuncionesHash import FrameBusquedaFuncionesHash

class FrameUnidad6(FramePersonalizado):

    def __init__(self, master):
        super().__init__(master=master)

        super().editar_titulo("Unidad 6 Metodos de busqueda")
        self.frame = None


        #COmponentes de algoritmos de ordenacion interno
        self.secuencial_arreglos_ordenados_componente = Componente("Secuencial ordenados", "Algoritmo de ordenación simple, compara elementos \nadyacentes y los intercambia si están en el orden\nincorrecto", master=self.canvas, funcion_nombre=self.secuencial_arreglos_ordenado)
        self.lista_componentes.append(self.secuencial_arreglos_ordenados_componente)

        self.secuencial_arreglos_desordenado_componente = Componente("Secuencial desordenado", "Algoritmo de ordenación simple, compara elementos \nadyacentes y los intercambia si están en el orden\nincorrecto", master=self.canvas, funcion_nombre=self.secuencial_arreglos_desordenado)
        self.lista_componentes.append(self.secuencial_arreglos_desordenado_componente)

        self.secuencial_listas_componentes = Componente("Secuencial listas", "Algoritmo de ordenación que se basa en la selección de\nun pivote y la división de la lista en dos subconjuntos", master=self.canvas, funcion_nombre=self.secuencial_listas)
        self.lista_componentes.append(self.secuencial_listas_componentes)

        self.busqueda_binaria_componente = Componente("Busqueda binaria", "Mejora el método de inserción al ordenar subgrupos de\nelementos con brechas decrecientes.", master=self.canvas, funcion_nombre=self.busqueda_binaria)
        self.lista_componentes.append(self.busqueda_binaria_componente)

        self.busqueda_funciones_hash_componente = Componente("Busqueda por funciones Hash", "Ordena los números procesando sus dígitos de menor a \nmayor o viceversa", master=self.canvas, funcion_nombre=self.busqueda_funciones_hash)
        self.lista_componentes.append(self.busqueda_funciones_hash_componente)



        super().agregar_lista_componentes(self.lista_componentes)

    def secuencial_arreglos_desordenado(self):
        self.frame = FrameSecuencialDesordenado(master=self, titulo="Secuencial desordenado")
        self.frame.place(x=0, y=0)

    def secuencial_arreglos_ordenado(self):
        self.frame = FrameSecuencialOrdenado(master=self, titulo="Secuencial ordenado")
        self.frame.place(x=0, y=0)

    def secuencial_listas(self):
        self.frame = FrameListas(master=self, titulo="Listas ligadas")
        self.frame.place(x=0, y=0)

    def busqueda_binaria(self):
        self.frame = FrameBusquedaBinaria(master=self, titulo="Busqueda binaria")
        self.frame.place(x=0, y=0)

    def busqueda_funciones_hash(self):
        self.frame = FrameBusquedaFuncionesHash(master=self, titulo="Por division")
        self.frame.place(x=0, y=0)
