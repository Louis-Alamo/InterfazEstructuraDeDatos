from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.componentes_multiples.MenuConBoton import MenuConBoton
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConBoton import CampoConBoton
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConTitulo import CampoConTitulo
from interfaz_grafica.componentes_personalizados.botones.BotonPersonalizado import BotonPersonalizado
from interfaz_grafica.frames_unidades.unidad4.arboles.Arbol import Arbol
from tkinter import Frame, messagebox
from interfaz_grafica.frames_unidades.unidad3.listas.Listas import Listas
class FrameArboles(FramePersonalizadoExtra):

    def __init__(self, master, titulo):
        super().__init__(master=master, titulo=titulo)
        self.comunicador = Listas()
        self.separacion = 180
        self.lista_widgets = []
        self.comunicador = Arbol()
        self.lista_opciones = ["Crear arbol", "Recorrido preorden", "Recorrido inorden", "Recorrido posorden"
                               ,"Busqueda", "Insertar", "Eliminar"]
        variable = self.lista_opciones[0]


        self.boton_seleccion = BotonSeleccionManera(master=self, nombre_boton="Simple",
                                                        nombre_funcion=self.seleccion_lista)
        self.boton_seleccion.place(x=39, y=75)

        self.menu = MenuConBoton(master=self.canvas, lista_opciones=self.lista_opciones, nombre_funcion_boton=self.opcion_seleccionada, variable=variable)
        self.lista_componentes.append(self.menu)

        self.frame_padre = Frame(self.canvas, width=602, bg="#FFFFFF")
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

        if opcion_seleccionada == "Crear arbol":
            self.crear_arbol()
        elif opcion_seleccionada == "Recorrido preorden":
            self.recorrido_preorden()

        elif opcion_seleccionada == "Recorrido inorden":
            self.recorrido_inorden()

        elif opcion_seleccionada == "Recorrido posorden":
            self.recorrido_posorden()

        elif opcion_seleccionada == "Busqueda":
            self.busqueda()

        elif opcion_seleccionada == "Insertar":
            self.insertar()

        elif opcion_seleccionada == "Eliminar":
            self.eliminar()

    def crear_arbol(self):
        self.campo = CampoConBoton(self.frame_padre, titulo="Ingrese el valor para el nodo raiz", nombre_boton="Crear", nombre_funcion=lambda:crear_arbol_funcion())
        self.campo.pack()
        self.lista_widgets.append(self.campo)

        def crear_arbol_funcion():
            dato = int(self.campo.obtener_datos())
            if self.comunicador.getBanderaCreacion():
                if messagebox.askyesno("Atencion", "Se creo una lista anteriormente si continua perdera la otra, desea continuar?"):
                    self.comunicador.crear_arbol(dato)
            else:
                self.comunicador.crear_arbol(dato)
                self.campo.limpiar_campo()

    def recorrido_preorden(self):
        self.area_texto = AreaDeInformacion(self.frame_padre, titulo="Mostrando arbol preorden")
        self.area_texto.pack()
        self.lista_widgets.append(self.area_texto)

        lista = self.comunicador.recorrer_preorden()
        self.area_texto.mostrar_informacion_estructura(lista)

    def recorrido_inorden(self):
        self.area_texto = AreaDeInformacion(self.frame_padre, titulo="Mostrando arbol inorden")
        self.area_texto.pack()
        self.lista_widgets.append(self.area_texto)

        lista = self.comunicador.recorrer_inorden()
        self.area_texto.mostrar_informacion_estructura(lista)


    def recorrido_posorden(self):
        self.area_texto = AreaDeInformacion(self.frame_padre, titulo="Mostrando arbol posorden")
        self.area_texto.pack()
        self.lista_widgets.append(self.area_texto)

        lista = self.comunicador.recorrer_posorden()
        self.area_texto.mostrar_informacion_estructura(lista)

    def busqueda(self):
        self.campo = CampoConBoton(self.frame_padre, titulo="Ingrese el valor del nodo a buscar", nombre_boton="Buscar", nombre_funcion=lambda:buscar_funcion())
        self.campo.pack()
        self.lista_widgets.append(self.campo)

        def buscar_funcion():
            dato = int(self.campo.obtener_datos())
            if self.comunicador.getBanderaCreacion() == False:
                messagebox.showinfo("Atencion", "No se a creado una arbol por lo que tiene que crearlo?")
            else:
                self.comunicador.buscar_elemento(dato)
        self.campo.limpiar_campo()

    def insertar(self):
        self.campo = CampoConBoton(self.frame_padre, titulo="Ingrese el valor del nodo a insertar", nombre_boton="Insertar", nombre_funcion=lambda:insertar_funcion())
        self.campo.pack()
        self.lista_widgets.append(self.campo)

        def insertar_funcion():
            dato = int(self.campo.obtener_datos())
            if self.comunicador.getBanderaCreacion() == False:
                messagebox.showinfo("Atencion", "No se a creado una arbol por lo que tiene que crearlo?")
            else:
                self.comunicador.insertar_elemento(dato)
            self.campo.limpiar_campo()

    def eliminar(self):
        self.campo = CampoConBoton(self.frame_padre, titulo="Ingrese el valor del nodo a eliminar", nombre_boton="Eliminar", nombre_funcion=lambda:insertar_funcion())
        self.campo.pack()
        self.lista_widgets.append(self.campo)

        def insertar_funcion():
            dato = int(self.campo.obtener_datos())
            if self.comunicador.getBanderaCreacion() == False:
                messagebox.showinfo("Atencion", "No se a creado una arbol por lo que tiene que crearlo?")
            else:
                self.comunicador.eliminar_elemento(dato)


        self.campo.limpiar_campo()