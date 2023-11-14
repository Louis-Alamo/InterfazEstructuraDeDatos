from interfaz_grafica.componentes_personalizados.botones.BotonPersonalizado import BotonPersonalizado
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConTitulo import CampoConTitulo
from tkinter import Frame, simpledialog
from interfaz_grafica.frames_unidades.unidad3.pilas.Pilas import Pila


class FramePilas(FramePersonalizadoExtra):

    def __init__(self, master, titulo):
        super().__init__(master=master, titulo=titulo)
        self.separacion = 100

        self.boton_selccion_pilas = BotonSeleccionManera(master=self, nombre_boton="Pilas",
                                                        nombre_funcion=self.seleccion)
        self.boton_selccion_pilas.place(x=39, y=75)


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

        self.area_texto = AreaDeInformacion(master = self.canvas, titulo="Aqui se muestra la pila")
        self.lista_componentes.append(self.area_texto)

        self.agregar_lista_componentes(self.lista_componentes)
        self.tamaño = simpledialog.askinteger("","Cual es el tamaño de tu lista?")
        self.pila = Pila(self.tamaño)
        self.seleccion()

    def seleccion(self):
        self.boton_selccion_pilas.seleccionado()
        self.limpiar_valores()

    def agregar_funcion(self):
        dato = int(self.campo.obtener_datos())
        self.pila.insertarElemento(dato)
        self.mostrar_pila()
        self.campo.limpiar_campo()

    def eliminar_funcion(self):
        self.pila.eliminarElemento()
        self.mostrar_pila()

    def mostrar_pila(self):
        self.area_texto.limpiar_area()
        self.lista1 = self.pila.getPila()
        self.lista = [f"{i} → " for i in self.lista1 if i is not None]

        # Eliminar la flecha después del último elemento
        if self.lista:
            self.lista[-1] = self.lista[-1].rstrip(" → ")

        self.area_texto.mostrar_texto_concatenado("".join(self.lista))

    def limpiar_valores(self):
        self.campo.limpiar_campo()
        self.pila.limpiar_valores()