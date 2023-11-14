from interfaz_grafica.componentes_personalizados.botones.BotonPersonalizado import BotonPersonalizado
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConTitulo import CampoConTitulo
from interfaz_grafica.frames_unidades.unidad3.colas.ColaCircular import ColaCircular
from interfaz_grafica.frames_unidades.unidad3.colas.ColaSimple import ColaSimple
from tkinter import Frame, simpledialog


class FrameColas(FramePersonalizadoExtra):

    def __init__(self, master, titulo):
        super().__init__(master=master, titulo=titulo)
        self.separacion = 100
        self.selecion = "simple"


        self.boton_selccion_simple = BotonSeleccionManera(master=self, nombre_boton="Simple",
                                                        nombre_funcion=self.seleccion_cola_simple)
        self.boton_selccion_simple.place(x=39, y=75)

        self.boton_selccion_cicular = BotonSeleccionManera(master=self, nombre_boton="Circular",
                                                        nombre_funcion=self.seleccion_cola_circular)
        self.boton_selccion_cicular.place(x=189, y=75)

        self.campo = CampoConTitulo(master=self.canvas, titulo="Ingresa un numero:")
        self.campo.campo.configure(width=602)
        self.lista_componentes.append(self.campo)

        self.frame = Frame(width=602, bg="#FFFFFF", height=44)
        self.lista_componentes.append(self.frame)

        self.agregar_boton = BotonPersonalizado(master=self.frame, nombre_boton="Agregar", funcion_boton=self.agregar_funcion)
        self.agregar_boton.pack(side="left", padx=20)

        self.eliminar_boton = BotonPersonalizado(master=self.frame, nombre_boton="Eliminar", funcion_boton=self.eliminar_funcion)
        self.eliminar_boton.configure(border_color="#FF0000", fg_color="#FFCCCC", text_color="#FF0000")
        self.eliminar_boton.pack(side="left", padx=20)

        self.area_texto = AreaDeInformacion(master = self.canvas, titulo="Aqui se muestra la cola")
        self.lista_componentes.append(self.area_texto)

        self.agregar_lista_componentes(self.lista_componentes)
        self.tamaño = simpledialog.askinteger("","Cual es el tamaño de tu lista?")

        self.comunicador = ColaSimple(self.tamaño)
        self.seleccion_cola_simple()

    def seleccion_cola_simple(self):
        self.seleccion = "simple"
        self.boton_selccion_cicular.deseleccionado()
        self.boton_selccion_simple.seleccionado()
        self.limpiar_valores()
        self.comunicador = ColaSimple(self.tamaño)


    def seleccion_cola_circular(self):
        self.seleccion = "circular"
        self.boton_selccion_simple.deseleccionado()
        self.boton_selccion_cicular.seleccionado()
        self.limpiar_valores()
        self.comunicador = ColaCircular(self.tamaño)

    def agregar_funcion(self):
        dato = int(self.campo.obtener_datos())
        if self.selecion == "simple":
            self.comunicador.insertarElemento(dato)
        elif self.selecion == "circular":
            self.comunicador.insertarElemento(dato)

        self.campo.limpiar_campo()
        self.mostrar_cola()

    def eliminar_funcion(self):
        if self.selecion == "simple":
            self.comunicador.eliminarElemento()
        elif self.selecion == "circular":
            self.comunicador.eliminarElemento()

        self.mostrar_cola()


    def mostrar_cola(self):
        self.area_texto.limpiar_area()
        self.lista1 = self.comunicador.getCola()
        self.lista = [f"{i} → " for i in self.lista1 if i is not None]

        # Eliminar la flecha después del último elemento
        if self.lista:
            self.lista[-1] = self.lista[-1].rstrip(" → ")

        self.area_texto.mostrar_texto_concatenado("".join(self.lista))

    def limpiar_valores(self):
        self.campo.limpiar_campo()
        self.comunicador.limpiar_valores()
        self.area_texto.limpiar_area()