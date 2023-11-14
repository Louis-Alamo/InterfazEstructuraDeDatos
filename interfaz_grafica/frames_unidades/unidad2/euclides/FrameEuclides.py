from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.botones.BotonPersonalizado import BotonPersonalizado
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConTitulo import CampoConTitulo
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from interfaz_grafica.frames_unidades.unidad2.euclides.Euclides import Euclides

class FrameEuclides(FramePersonalizadoExtra):

    def __init__(self,master, titulo):
        super().__init__(master=master, titulo=titulo)
        self.separacion = 100
        self.seleccion = "iterativo"
        self.comunicador = Euclides()

        self.boton_selccion_iterativo = BotonSeleccionManera(master=self, nombre_boton="Iterativo",
                                                        nombre_funcion=self.seleccion_iterativo)
        self.boton_selccion_iterativo.place(x=39, y=75)

        self.boton_selccion_recursivo = BotonSeleccionManera(master=self, nombre_boton="Recursivo",
                                                             nombre_funcion=self.seleccion_recursivo)
        self.boton_selccion_recursivo.place(x=189, y=75)

        self.campo1 = CampoConTitulo(master=self.canvas, titulo="Numero 1")
        self.campo1.campo.configure(width=602)
        self.lista_componentes.append(self.campo1)

        self.campo2 = CampoConTitulo(master=self.canvas, titulo="Numero 2")
        self.campo2.campo.configure(width=602)
        self.lista_componentes.append(self.campo2)

        self.boton_calcular = BotonPersonalizado(master=self.canvas, funcion_boton=self.resolver_ecuclides, nombre_boton="Calcular")
        self.boton_calcular.configure(width=602)
        self.lista_componentes.append(self.boton_calcular)

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


    def resolver_ecuclides(self):
        resultado = 0
        a = int(self.campo1.obtener_datos())
        b = int(self.campo2.obtener_datos())

        if self.seleccion == "iterativo":
            resultado = self.comunicador.euclides_iterativo(a,b)
        elif self.seleccion == "recursivo":
            resultado = self.comunicador.euclides_recursivo(a,b)

        self.area_texto.mostrar_texto_concatenado(f"El maximo comun divisor es: {resultado}")


    def limpiar_valores(self):
        self.campo1.limpiar_campo()
        self.campo2.limpiar_campo()
        self.area_texto.limpiar_area()