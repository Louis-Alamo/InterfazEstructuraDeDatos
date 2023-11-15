from interfaz_grafica.componentes_personalizados.frames.FramePersonalizado import FramePersonalizado
from interfaz_grafica.componentes_personalizados.componentes_multiples.Componente import Componente
from interfaz_grafica.frames_unidades.unidad4.arboles.FrameArboles import FrameArboles

class FrameUnidad4(FramePersonalizado):

    def __init__(self,master):
        super().__init__(master=master)

        self.editar_titulo("Unidad 4 Estructuras no lineales")

        self.arboles_componente = Componente("Arboles","Descripcion",master=self.canvas, funcion_nombre=self.arboles_funcion)
        self.lista_componentes.append(self.arboles_componente)

        self.agregar_lista_componentes(self.lista_componentes)

    def arboles_funcion(self):
        self.frame = FrameArboles(master=self, titulo="Arboles")
        self.frame.place(x=0, y=0)