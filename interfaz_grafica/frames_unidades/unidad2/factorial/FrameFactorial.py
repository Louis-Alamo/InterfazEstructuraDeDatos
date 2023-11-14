from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConBoton import CampoConBoton
from interfaz_grafica.frames_unidades.unidad2.factorial.Factorial import Factorial

class FrameFactorial(FramePersonalizadoExtra):

    def __init__(self,master, titulo):
        super().__init__(master=master, titulo=titulo)
        self.separacion = 150
        self.seleccion = "iterativo"
        self.comunicador = Factorial()

        self.boton_selccion_iterativo = BotonSeleccionManera(master=self, nombre_boton="Iterativo",
                                                        nombre_funcion=self.seleccion_iterativo)
        self.boton_selccion_iterativo.place(x=39, y=75)

        self.boton_selccion_recursivo = BotonSeleccionManera(master=self, nombre_boton="Recursivo",
                                                             nombre_funcion=self.seleccion_recursivo)
        self.boton_selccion_recursivo.place(x=189, y=75)


        self.campo = CampoConBoton(master=self.canvas, titulo="Ingresa el titulo", nombre_boton="Calcular", nombre_funcion=self.resolver_factorial)
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


    def resolver_factorial(self):
        resultado = 0
        numero = int(self.campo.obtener_datos())
        if self.seleccion == "iterativo":
            resultado = self.comunicador.factorial_iterativo(numero)
        elif self.seleccion == "recursivo":
            resultado = self.comunicador.factorial_recursivo(numero)

        self.area_texto.mostrar_texto_concatenado(resultado)


    def limpiar_valores(self):
        self.campo.limpiar_campo()
        self.area_texto.limpiar_area()
