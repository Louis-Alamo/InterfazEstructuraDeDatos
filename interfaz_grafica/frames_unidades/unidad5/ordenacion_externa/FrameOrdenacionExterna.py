from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConTitulo import CampoConTitulo
from interfaz_grafica.componentes_personalizados.botones.BotonPersonalizado import BotonPersonalizado
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from interfaz_grafica.frames_unidades.unidad5.ordenacion_externa.MezclaNatural import MezclaNatural
from interfaz_grafica.frames_unidades.unidad5.ordenacion_externa.Intercalacion import Intercalacion
from interfaz_grafica.frames_unidades.unidad5.ordenacion_externa.MezclaDirecta import MezclaDirecta
class FrameOrdenacionExterna(FramePersonalizadoExtra):

    def __init__(self,master,titulo):
        super().__init__(master=master, titulo=titulo)
        self.separacion = 100
        self.seleccion = "natural"
        self.comunicador = None
        self.boton_seleccion_natural = BotonSeleccionManera(master=self, nombre_boton="Mezcla natural",
                                                        nombre_funcion=self.seleccion_natural)
        self.boton_seleccion_natural.place(x=39, y=75)

        self.boton_seleccion_intercalacion = BotonSeleccionManera(master=self, nombre_boton="Intercalacion",
                                                             nombre_funcion=self.seleccion_intercalacion)
        self.boton_seleccion_intercalacion.place(x=189, y=75)

        self.boton_seleccion_mezcla = BotonSeleccionManera(master=self, nombre_boton="mezcla directa",
                                                             nombre_funcion=self.seleccion_mezcla)
        self.boton_seleccion_mezcla.place(x=339, y=75)

        self.boton_seleccion_natural.seleccionado()

        self.campo1 = CampoConTitulo(master=self.canvas, titulo="Ingrese los valores del archivo 1 separados por comas")
        self.campo1.campo.configure(width=602)
        self.lista_componentes.append(self.campo1)


        self.boton_resolver = BotonPersonalizado(master=self.canvas, funcion_boton=self.seleccion_opcion, nombre_boton="Ordenar")
        self.lista_componentes.append(self.boton_resolver)

        self.area_texto = AreaDeInformacion(master=self.canvas, titulo="Valores ordenados")
        self.area_texto.configure(height=151)
        self.area_texto.area_texto.configure(height=120)
        self.area_texto.scrollbar.configure(height=114)
        self.lista_componentes.append(self.area_texto)


        self.agregar_lista_componentes(self.lista_componentes)
        self.seleccion_natural()

    def seleccion_natural(self):
        self.seleccion = "natural"
        self.boton_seleccion_mezcla.deseleccionado()
        self.boton_seleccion_intercalacion.deseleccionado()
        self.boton_seleccion_natural.seleccionado()
        self.limpiar_valores()

    def limpiar_frame_padre(self):
        pass
    def seleccion_intercalacion(self):
        self.seleccion = "intercalacion"
        self.boton_seleccion_mezcla.deseleccionado()
        self.boton_seleccion_intercalacion.seleccionado()
        self.boton_seleccion_natural.deseleccionado()
        self.limpiar_valores()
    def seleccion_mezcla(self):
        self.seleccion = "mezcla"
        self.boton_seleccion_mezcla.seleccionado()
        self.boton_seleccion_intercalacion.deseleccionado()
        self.boton_seleccion_natural.deseleccionado()
        self.limpiar_valores()


    def seleccion_opcion(self):
        datos = self.campo1.obtener_datos().replace(',', ' ')
        with open('F3.txt','w') as archivo3:
            archivo3.write(datos)

        if self.seleccion == "natural":
            pass
        elif self.seleccion == "intercalacion":
            pass

        elif self.seleccion == "mezcla":
            self.comunicador = MezclaDirecta(ruta_archivo='F3.txt')
            self.comunicador.mezcla_directa()
            historial = self.comunicador.obtener_informacion()
            self.area_texto.mostrar_texto_concatenado(historial)
            print("No imprimio")
            print("\nArchivo ordenado (archivo3.txt):")
            with open('F3.txt', 'r') as f:
                print(f.read())



