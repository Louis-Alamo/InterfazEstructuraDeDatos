from interfaz_grafica.componentes_personalizados.frames.FramePersonalizado import FramePersonalizado
from interfaz_grafica.componentes_personalizados.componentes_multiples.Componente import Componente
from interfaz_grafica.frames_unidades.unidad3.pilas.FramePilas import FramePilas
from interfaz_grafica.frames_unidades.unidad3.colas.FrameColas import FrameColas
class FrameUnidad3(FramePersonalizado):

    def __init__(self,master):
        super().__init__(master=master)

        self.editar_titulo("Unidad 3 Estructuras lineales")


        self.colas_componente = Componente("Colas","Descripcion",master=self.canvas, funcion_nombre=self.colas_funcion)
        self.lista_componentes.append(self.colas_componente)

        self.lista_componente_interfaz = Componente("Listas","Descripcion",master=self.canvas, funcion_nombre=self.listas_funcion)
        self.lista_componentes.append(self.lista_componente_interfaz)

        self.pilas_componente = Componente("Pilas","Descripcion",master=self.canvas, funcion_nombre=self.pilas_funcion)
        self.lista_componentes.append(self.pilas_componente)

        self.agregar_lista_componentes(self.lista_componentes)

    def colas_funcion(self):
        self.frame = FrameColas(master=self, titulo="Colas")
        self.frame.place(x=0, y=0)

    def listas_funcion(self):
        pass

    def pilas_funcion(self):
        self.frame = FramePilas(master=self, titulo="Pilas")
        self.frame.place(x=0, y=0)
