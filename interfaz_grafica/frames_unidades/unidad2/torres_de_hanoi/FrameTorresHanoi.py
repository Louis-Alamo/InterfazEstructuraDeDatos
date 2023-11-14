from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConBoton import CampoConBoton
from interfaz_grafica.componentes_personalizados.componentes_multiples.CuadroInformacion import cuadroInformacion
from interfaz_grafica.frames_unidades.unidad2.torres_de_hanoi.TorresHanoi import TorresHanoi
from PIL import Image

class FrameTorresDeHanoi(FramePersonalizadoExtra):

    def __init__(self,master, titulo):
        super().__init__(master=master, titulo=titulo)
        self.separacion = 170
        self.seleccion = "iterativo"
        self.valor = 0
        self.comunicador = TorresHanoi()

        self.boton_selccion_iterativo = BotonSeleccionManera(master=self, nombre_boton="Iterativo",
                                                        nombre_funcion=self.seleccion_iterativo)
        self.boton_selccion_iterativo.place(x=39, y=75)

        self.boton_selccion_recursivo = BotonSeleccionManera(master=self, nombre_boton="Recursivo",
                                                             nombre_funcion=self.seleccion_recursivo)
        self.boton_selccion_recursivo.place(x=189, y=75)

        self.campo = CampoConBoton(master = self.canvas, titulo="Ingresa la cantidad de discos", nombre_boton="Calcular", nombre_funcion=self.resolver_torres)
        self.lista_componentes.append(self.campo)

        self.area_texto = AreaDeInformacion(master=self.canvas, titulo="Resultados")
        self.area_texto.configure(height=152)
        self.area_texto.area_texto.configure(height=120)
        self.area_texto.scrollbar.configure(height=114)
        self.lista_componentes.append(self.area_texto)

        self.imagen = Image.open("../imagenes/Movimientos.png")
        self.cuadro_informativo = cuadroInformacion(master=self.canvas, imagen=self.imagen, titulo="Movimientos", valor=self.valor)
        self.lista_componentes.append(self.cuadro_informativo)

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

    def resolver_torres(self):
        resultado = []
        discos = int(self.campo.obtener_datos())
        if self.seleccion == "iterativo":
            resultado = self.comunicador.hanoi_iterativo(discos, 'A', 'C', 'B')

        elif self.seleccion == "recursivo":
            resultado = self.comunicador.hanoi_recursivo(discos,'A', 'C', 'B')
        self.valor = len(resultado)
        cadena_movimientos = "\n".join(resultado)
        self.area_texto.mostrar_texto_concatenado(cadena_movimientos)
        self.cuadro_informativo.cambiar_valor(self.valor)

    def limpiar_valores(self):
        self.campo.limpiar_campo()
        self.area_texto.limpiar_area()
        self.valor = 0
        self.cuadro_informativo.cambiar_valor(self.valor)