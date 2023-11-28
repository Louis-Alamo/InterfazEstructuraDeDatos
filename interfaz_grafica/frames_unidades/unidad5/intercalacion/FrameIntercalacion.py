from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConTitulo import CampoConTitulo
from interfaz_grafica.componentes_personalizados.botones.BotonPersonalizado import BotonPersonalizado
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from interfaz_grafica.frames_unidades.unidad5.ordenacion_externa.MezclaDirecta import MezclaDirecta
from interfaz_grafica.frames_unidades.unidad5.intercalacion.Intercalacion import Intercalacion
from tkinter import messagebox
class FrameIntercalacion(FramePersonalizadoExtra):

    def __init__(self,master,titulo):
        super().__init__(master=master, titulo=titulo)
        self.separacion = 100

        self.comunicador = None
        self.boton_seleccion = BotonSeleccionManera(master=self, nombre_boton="Intercalacion",
                                                            nombre_funcion=self.seleccion)
        self.boton_seleccion.place(x=39, y=75)

        self.boton_seleccion.seleccionado()

        self.campo1 = CampoConTitulo(master=self.canvas, titulo="Ingrese los valores del archivo 1 separados por comas")
        self.campo1.campo.configure(width=602)
        self.lista_componentes.append(self.campo1)

        self.campo2 = CampoConTitulo(master=self.canvas, titulo="Ingrese los valores del archivo 2 separados por comas")
        self.campo2.campo.configure(width=602)
        self.lista_componentes.append(self.campo2)

        self.boton_resolver = BotonPersonalizado(master=self.canvas, funcion_boton=self.resolver,
                                                 nombre_boton="Ordenar")
        self.lista_componentes.append(self.boton_resolver)

        self.area_texto = AreaDeInformacion(master=self.canvas, titulo="Valores ordenados")
        self.area_texto.configure(height=151)
        self.area_texto.area_texto.configure(height=120)
        self.area_texto.scrollbar.configure(height=114)
        self.lista_componentes.append(self.area_texto)


        self.agregar_lista_componentes(self.lista_componentes)
        self.seleccion()

    def seleccion(self):
        self.boton_seleccion.seleccionado()
    def resolver(self):
        datos = None
        datos = self.campo1.obtener_datos()
        datos = datos.replace("," ,"\n")
        with open('F1.txt' , 'w') as archivo1:
            archivo1.write(datos)

        datos = self.campo2.obtener_datos()
        datos = datos.replace(",", "\n")
        with open('F2.txt' , 'w') as archivo2:
            archivo2.write(datos)


        self.comunicador = Intercalacion(nombre_archivo1='F1.txt', nombre_archivo2='F2.txt', nombre_archivo_resultante='F3.txt')
        self.comunicador.inicioAlgoritmo()
        historial = self.comunicador.get_log()
        self.area_texto.mostrar_texto_concatenado(historial)