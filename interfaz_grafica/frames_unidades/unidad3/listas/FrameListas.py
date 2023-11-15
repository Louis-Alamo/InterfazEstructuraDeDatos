from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.componentes_multiples.MenuConBoton import MenuConBoton
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConBoton import CampoConBoton
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from tkinter import Frame, messagebox
from interfaz_grafica.frames_unidades.unidad3.listas.Listas import Listas
class FrameListas(FramePersonalizadoExtra):

    def __init__(self, master, titulo):
        super().__init__(master=master, titulo=titulo)
        self.comunicador = Listas()
        self.separacion = 100
        self.lista_widgets = []
        self.lista_opciones = ["Crear inicio", "Crear final", "Recorrer iterativo", "Recorrer recursivo", "Inserta inicio"
                               "Inserta final", "Inserta antes de", "Inserta despues de", "Elimina inicio", "Elimina final"]
        variable = self.lista_opciones[0]


        self.boton_seleccion = BotonSeleccionManera(master=self, nombre_boton="Simple",
                                                        nombre_funcion=self.seleccion_lista)
        self.boton_seleccion.place(x=39, y=75)

        self.menu = MenuConBoton(master=self.canvas, lista_opciones=self.lista_opciones, nombre_funcion_boton=self.opcion_seleccionada, variable=variable)
        self.lista_componentes.append(self.menu)

        self.frame_padre = Frame(self.canvas, width=602)
        self.lista_componentes.append(self.frame_padre)

        self.agregar_lista_componentes(self.lista_componentes)
        self.seleccion_lista()

    def limpiar_frame_padre(self):
        for widget in self.lista_widgets:
            widget.destroy()
        self.lista_widgets = []

    def seleccion_lista(self):
        self.boton_seleccion.seleccionado()
        self.limpiar_valores()


    def opcion_seleccionada(self):
        opcion_seleccionada = self.menu.getSeleccion()
        self.limpiar_frame_padre()
        if opcion_seleccionada == "Crear inicio":
            self.crear_inicio()

        elif opcion_seleccionada == "Crear final":
            self.crear_final()

        elif opcion_seleccionada == "Recorrer iterativo":
            self.recorrer_iterativo()

        elif opcion_seleccionada == "Recorrer recursivo":
            self.recorrer_recursivo()

        elif opcion_seleccionada == "Inserta inicio":
            self.insertar_inicio_interfaz()

        elif opcion_seleccionada == "Inserta final":
            self.inserta_final_interfaz()

        elif opcion_seleccionada == "Inserta antes de":
            self.inserta_antes_de_interfaz()


        elif opcion_seleccionada == "Inserta después de":
            self.inserta_antes_de_interfaz()

        elif opcion_seleccionada == "Elimina inicio":
            self.elimina_inicio_interfaz()

        elif opcion_seleccionada == "Elimina final":
            self.elimina_final_interfaz()

        elif opcion_seleccionada == "Elimina nodo x":
            self.elimina_nodo_x_interfaz()

        elif opcion_seleccionada == "Elimina antes de":
            self.elimina_antes_de_interfaz()

        elif opcion_seleccionada == "Elimina después de":
            self.elimina_despues_de_interfaz()

        elif opcion_seleccionada == "Búsqueda desordenada":
            self.busqueda_desordenadas_interfaz()

        elif opcion_seleccionada == "Búsqueda ordenada":
            self.busqueda_ordenadas_interfaz()

        elif opcion_seleccionada == "Búsqueda recursiva":
            self.busqueda_recursivas_interfaz()

    def crear_inicio(self):
        print("Entro")
        self.campo = CampoConBoton(self.frame_padre, titulo="Ingrese el valor de crear inicio", nombre_boton="Crear", nombre_funcion=lambda:crear_inicio_funcion())
        self.campo.pack()
        self.lista_widgets.append(self.campo)
        def crear_inicio_funcion():
            dato = int(self.campo.obtener_datos())
            if self.comunicador.obtener_bandera_creacion():
                if messagebox.askyesno("Atencion", "Se creo una lista anteriormente si continua perdera la otra, desea continuar?"):
                    self.comunicador.agregar_al_principio(dato)
            else:
                self.comunicador.agregar_al_final(dato)

            self.campo.limpiar_campo()

    def crear_final(self):
        print("Entro")
        self.campo = CampoConBoton(self.frame_padre, titulo="Ingrese el valor de crear final", nombre_boton="Crear", nombre_funcion=lambda:crear_final_funcion())
        self.campo.pack()
        self.lista_widgets.append(self.campo)

        def crear_final_funcion():
            dato = int(self.campo.obtener_datos())
            if self.comunicador.getBanderaCreacion():
                if messagebox.askyesno("Atencion", "Se creo una lista anteriormente si continua perdera la otra, desea continuar?"):
                    self.comunicador.crear_lista(dato)
            else:
                self.comunicador.crear_lista(dato)

            self.campo.limpiar_campo()

    def recorrer_iterativo(self):
        self.area_texto = AreaDeInformacion(self.frame_padre, titulo="Mostrando lista iterativo")
        self.area_texto.pack()
        self.lista_widgets.append(self.area_texto)
        lista = self.comunicador.recorrer_iterativo()
        self.area_texto.mostrar_informacion_estructura(lista)

    def recorrer_recursivo(self):
        self.area_texto = AreaDeInformacion(self.frame_padre, titulo="Mostrando lista iterativo")
        self.area_texto.pack()
        self.lista_widgets.append(self.area_texto)
        lista = self.comunicador.recorrer_recursivo()
        self.area_texto.mostrar_informacion_estructura(lista)

    def insertar_inicio(self):
        pass

    def insertar_final(self):
        pass

    def insertar_antes_de(self):
        pass

    def insertar_despues_de(self):
        pass

    def elimina_inicio(self):
        pass

    def elimina_final(self):
        pass


