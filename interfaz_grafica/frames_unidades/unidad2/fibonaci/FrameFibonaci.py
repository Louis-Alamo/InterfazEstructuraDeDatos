from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConBoton import CampoConBoton
from interfaz_grafica.frames_unidades.unidad2.fibonaci.Fibonaci import Fibonaci
class FrameFibonaci(FramePersonalizadoExtra):

    def __init__(self, master, titulo):
        super().__init__(master=master, titulo=titulo)
        self.separacion = 100
        self.seleccion = "iterativo"
        self.comunicador = Fibonaci()

        self.boton_selccion_iterativo = BotonSeleccionManera(master=self, nombre_boton="Iterativo",
                                                              nombre_funcion=self.seleccion_iterativo)
        self.boton_selccion_iterativo.place(x=39, y=75)

        self.boton_selccion_recursivo = BotonSeleccionManera(master=self, nombre_boton="Recursivo",
                                                             nombre_funcion=self.seleccion_recursivo)
        self.boton_selccion_recursivo.place(x=189, y=75)

        self.campo = CampoConBoton(master=self.canvas, titulo="Ingresa el titulo", nombre_boton="Calcular",
                                   nombre_funcion=self.resolver_fibonaci)
        self.lista_componentes.append(self.campo)

        self.area_texto = AreaDeInformacion(master=self.canvas, titulo="Resultados")
        self.lista_componentes.append(self.area_texto)

        self.agregar_lista_componentes(self.lista_componentes)

        self.seleccion_iterativo()

    def seleccion_iterativo(self):
        self.seleccion = "iterativo"
        self.boton_selccion_recursivo.deseleccionado()
        self.boton_selccion_iterativo.seleccionado()
        self.limpiar_valores()

    def seleccion_recursivo(self):
        self.seleccion = "recursivo"
        self.boton_selccion_iterativo.deseleccionado()
        self.boton_selccion_recursivo.seleccionado()
        self.limpiar_valores()

    def resolver_fibonaci(self):
        self.area_texto.limpiar_area()
        numero = int(self.campo.obtener_datos())
        resultado = ""
        if self.seleccion == "iterativo":
            self.area_texto.mostrar_texto_concatenado( self.comunicador.fibonacci_iterativo(numero))
        elif self.seleccion == "recursivo":
            self.area_texto.mostrar_texto_concatenado(self.comunicador.fibonacci_recursivo(numero))



    def limpiar_valores(self):
        self.campo.limpiar_campo()
        self.area_texto.limpiar_area()
