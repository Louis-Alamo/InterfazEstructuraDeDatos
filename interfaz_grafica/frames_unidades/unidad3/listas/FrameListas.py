from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.componentes_multiples.MenuConBoton import MenuConBoton
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConBoton import CampoConBoton
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConTitulo import CampoConTitulo
from interfaz_grafica.componentes_personalizados.botones.BotonPersonalizado import BotonPersonalizado
from tkinter import Frame, messagebox
from interfaz_grafica.frames_unidades.unidad3.listas.Listas import Listas
class FrameListas(FramePersonalizadoExtra):

    def __init__(self, master, titulo):
        super().__init__(master=master, titulo=titulo)
        self.comunicador = Listas()
        self.separacion = 180
        self.lista_widgets = []
        self.lista_opciones = ["Crear inicio", "Crear final", "Recorrer iterativo", "Recorrer recursivo", "Inserta inicio",
                               "Inserta final", "Inserta antes de", "Inserta despues de", "Elimina inicio", "Elimina final","Elimina nodo x",
                               "Elimina antes de","Elimina después de","Búsqueda desordenada","Búsqueda ordenada","Búsqueda recursiva"]
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

        if opcion_seleccionada == "Crear inicio":
            self.crear_inicio()

        elif opcion_seleccionada == "Recorrer iterativo":
            self.recorrer_iterativo()

        elif opcion_seleccionada == "Recorrer recursivo":
            self.recorrer_recursivo()

        elif opcion_seleccionada == "Inserta inicio":
            self.insertar_inicio()
        elif opcion_seleccionada == "Inserta final":
            self.insertar_final()

        elif opcion_seleccionada == "Inserta antes de":
            self.insertar_antes_de()

        elif opcion_seleccionada == "Inserta despues de":
            self.insertar_despues_de()

        elif opcion_seleccionada == "Elimina inicio":
            self.elimina_inicio()

        elif opcion_seleccionada == "Elimina final":
            self.elimina_final()

        elif opcion_seleccionada == "Elimina nodo x":
            self.elimina_nodo_x()

        elif opcion_seleccionada == "Elimina antes de":
            self.elimina_antes_de()

        elif opcion_seleccionada == "Elimina después de":
            self.elimina_despues_de()

        elif opcion_seleccionada == "Búsqueda desordenada":
            self.busqueda_desordenada()

        elif opcion_seleccionada == "Búsqueda ordenada":
            self.busqueda_ordenada()

        elif opcion_seleccionada == "Búsqueda recursiva":
            self.busqueda_recursiva()

    #Metodo para crear la lista
    def crear_inicio(self):
        self.campo = CampoConBoton(self.frame_padre, titulo="Ingrese el valor de crear inicio", nombre_boton="Crear", nombre_funcion=lambda:crear_inicio_funcion())
        self.campo.pack()
        self.lista_widgets.append(self.campo)

        def crear_inicio_funcion():
            dato = int(self.campo.obtener_datos())
            if self.comunicador.getBanderaCreacion():
                if messagebox.askyesno("Atencion", "Se creo una lista anteriormente si continua perdera la otra, desea continuar?"):
                    self.comunicador.crear_lista(dato)

            else:
                self.comunicador.crear_lista(dato)

            self.campo.limpiar_campo()


    #Metodos para recorrer la lista
    def recorrer_iterativo(self):
        self.area_texto = AreaDeInformacion(self.frame_padre, titulo="Mostrando lista iterativo")
        self.area_texto.pack()
        self.lista_widgets.append(self.area_texto)
        lista = self.comunicador.recorrer_iterativo()
        self.area_texto.mostrar_informacion_estructura(lista)
    def recorrer_recursivo(self):
        self.area_texto = AreaDeInformacion(self.frame_padre, titulo="Mostrando lista recursivo")
        self.area_texto.pack()
        self.lista_widgets.append(self.area_texto)
        lista = self.comunicador.recorrer_recursivo()
        self.area_texto.mostrar_informacion_estructura(lista)


    #Metodos para insertar
    def insertar_inicio(self):
        self.campo = CampoConBoton(self.frame_padre, titulo="Ingrese el valor a insertar inicio", nombre_boton="Insertar", nombre_funcion=lambda:insertar_inicio_funcion())
        self.campo.pack()
        self.lista_widgets.append(self.campo)

        def insertar_inicio_funcion():
            dato = int(self.campo.obtener_datos())
            self.comunicador.insertar_inicio(dato)
            self.campo.limpiar_campo()
    def insertar_final(self):
        self.campo = CampoConBoton(self.frame_padre, titulo="Ingrese el valor a insertar final", nombre_boton="Insertar", nombre_funcion=lambda:insertar_final_funcion())
        self.campo.pack()
        self.lista_widgets.append(self.campo)

        def insertar_final_funcion():
            dato = int(self.campo.obtener_datos())
            self.comunicador.insertar_final(dato)
            self.campo.limpiar_campo()
    def insertar_antes_de(self):
        self.campo1 = CampoConTitulo(master=self.frame_padre, titulo="Ingrese el valor a insertar")
        self.campo1.pack()

        self.campo2 = CampoConTitulo(master=self.frame_padre, titulo="Ingrese el valor de referencia")
        self.campo2.pack(pady=10)

        self.boton = BotonPersonalizado(master=self.frame_padre, funcion_boton=lambda: insertar_antes_de(), nombre_boton="Buscar e insertar")
        self.boton.pack(pady=10)

        self.lista_widgets.append(self.campo1)
        self.lista_widgets.append(self.campo2)
        self.lista_widgets.append(self.boton)

        def insertar_antes_de():
            dato = int(self.campo1.obtener_datos())
            referencia = int(self.campo2.obtener_datos())

            self.comunicador.insertar_antes_de(dato, referencia)

            self.campo1.limpiar_campo()
            self.campo2.limpiar_campo()
    def insertar_despues_de(self):
        print("si")
        self.campo1 = CampoConTitulo(master=self.frame_padre, titulo="Ingrese el valor a insertar")
        self.campo1.pack()

        self.campo2 = CampoConTitulo(master=self.frame_padre, titulo="Ingrese el valor de referencia")
        self.campo2.pack(pady=10)

        self.boton = BotonPersonalizado(master=self.frame_padre, funcion_boton=lambda: insertar_despues_de(), nombre_boton="Buscar e insertar")
        self.boton.pack(pady=10)

        self.lista_widgets.append(self.campo1)
        self.lista_widgets.append(self.campo2)
        self.lista_widgets.append(self.boton)

        def insertar_despues_de():
            dato = int(self.campo1.obtener_datos())
            referencia = int(self.campo2.obtener_datos())

            self.comunicador.insertar_despues_de(dato, referencia)

            self.campo1.limpiar_campo()
            self.campo2.limpiar_campo()


    #Metodos de eliminacion
    def elimina_inicio(self):
        self.boton = BotonPersonalizado(self.frame_padre, funcion_boton=lambda: eliminar_inicio_funcion(), nombre_boton="Eliminar valor")
        self.boton.pack()
        self.lista_widgets.append(self.boton)

        def eliminar_inicio_funcion():
            self.comunicador.eliminar_inicio()
    def elimina_final(self):
        self.boton = BotonPersonalizado(self.frame_padre, funcion_boton=lambda: eliminar_final_funcion(), nombre_boton="Eliminar valor")
        self.boton.pack()
        self.lista_widgets.append(self.boton)

        def eliminar_final_funcion():
            self.comunicador.eliminar_final()
    def elimina_nodo_x(self):
        self.campo = CampoConBoton(self.frame_padre, titulo="Ingrese el valor a eliminar", nombre_boton="Insertar", nombre_funcion=lambda:eliminar_nodo_x_funcion())
        self.campo.pack()
        self.lista_widgets.append(self.campo)

        def eliminar_nodo_x_funcion():
            dato = int(self.campo.obtener_datos())
            self.comunicador.elimina_nodo_x(dato)
            self.campo.limpiar_campo()
    def elimina_despues_de(self):
        self.campo = CampoConBoton(self.frame_padre, titulo="Ingrese el valor de referencia", nombre_boton="Eliminar", nombre_funcion=lambda:elimina_despues_de_funcion())
        self.campo.pack()
        self.lista_widgets.append(self.campo)

        def elimina_despues_de_funcion():
            dato = int(self.campo.obtener_datos())
            self.comunicador.elimina_despues_de(dato)
            self.campo.limpiar_campo()
    def elimina_antes_de(self):
        self.campo = CampoConBoton(self.frame_padre, titulo="Ingrese el valor de referencia", nombre_boton="Eliminar", nombre_funcion=lambda:elimina_antes_de_funcion())
        self.campo.pack()
        self.lista_widgets.append(self.campo)

        def elimina_antes_de_funcion():
            dato = int(self.campo.obtener_datos())
            self.comunicador.elimina_antes_de(dato)
            self.campo.limpiar_campo()


    #metodos de busqueda
    def busqueda_ordenada(self):
        messagebox.showinfo("Atecion", "Para que esta funcion sirva la lista debe tener los elementos ordenados ")
        self.campo = CampoConBoton(self.frame_padre, titulo="Ingrese el valor a buscar", nombre_boton="Buscar", nombre_funcion=lambda:busqueda_ordenada_funcion())
        self.campo.pack()
        self.lista_widgets.append(self.campo)

        def busqueda_ordenada_funcion():
            dato = int(self.campo.obtener_datos())
            self.comunicador.busqueda_ordenada(dato)
            self.campo.limpiar_campo()
    def busqueda_desordenada(self):
        self.campo = CampoConBoton(self.frame_padre, titulo="Ingrese el valor a buscar", nombre_boton="Buscar", nombre_funcion=lambda:busqueda_desordenada_funcion())
        self.campo.pack()
        self.lista_widgets.append(self.campo)

        def busqueda_desordenada_funcion():
            dato = int(self.campo.obtener_datos())
            self.comunicador.busqueda_desordenada(dato)
            self.campo.limpiar_campo()
    def busqueda_recursiva(self):
        self.campo = CampoConBoton(self.frame_padre, titulo="Ingrese el valor a buscar", nombre_boton="Buscar", nombre_funcion=lambda:busqueda_recursiva_funcion())
        self.campo.pack()
        self.lista_widgets.append(self.campo)

        def busqueda_recursiva_funcion():
            dato = int(self.campo.obtener_datos())
            self.comunicador.busqueda_recursivas(valor_buscar=dato)
            self.campo.limpiar_campo()
