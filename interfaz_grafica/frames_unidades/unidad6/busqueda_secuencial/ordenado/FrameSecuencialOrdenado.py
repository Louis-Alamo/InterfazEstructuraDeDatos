from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConBoton import CampoConBoton
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from interfaz_grafica.frames_unidades.unidad6.busqueda_secuencial.ordenado.BusquedaSecuencialOrdenado import BusquedaSecuencialOrdenado
from tkinter import Frame, simpledialog, messagebox
class FrameSecuencialOrdenado(FramePersonalizadoExtra):

    def __init__(self, master, titulo):
        super().__init__(master=master, titulo=titulo)
        self.seleccion = "iterativo"
        self.separacion = 100
        self.mensajero = BusquedaSecuencialOrdenado()

        self.iterativo_boton = BotonSeleccionManera(master=self, nombre_boton="iterativo",nombre_funcion=self.seleccion_iterativo)
        self.iterativo_boton.place(x=39, y=75)

        self.recursivo_boton = BotonSeleccionManera(master=self, nombre_boton="recursivo", nombre_funcion=self.seleccion_recursivo)
        self.recursivo_boton.place(x=189, y=75)

        self.campo = CampoConBoton(master=self.canvas, titulo="Ingrese los valores del arreglo", nombre_boton="Agregar", nombre_funcion=self.obtener_datos)
        self.lista_componentes.append(self.campo)

        self.linea = Frame(master=self.canvas,  width=663,height=3, bg="#4E458E")
        self.lista_componentes.append(self.linea)

        self.campo2  = CampoConBoton(master=self.canvas, titulo="Ingrese el valor a buscar", nombre_boton="Buscar", nombre_funcion=self.opcion_seleccionada)
        self.lista_componentes.append(self.campo2)

        self.area_texto = AreaDeInformacion(master=self.canvas, titulo="Resultado")
        self.lista_componentes.append(self.area_texto)


        self.agregar_lista_componentes(self.lista_componentes)

        self.tamaño = simpledialog.askinteger("Nota", "Dame el tamaño de tu arreglo")
        self.arreglo = []
        self.contador = 0


        self.seleccion_iterativo()

    def seleccion_iterativo(self):
        self.seleccion = "iterativo"
        self.iterativo_boton.seleccionado()
        self.recursivo_boton.deseleccionado()
        self.limpiar_valores()

    def seleccion_recursivo(self):
        self.seleccion = "recursivo"
        self.recursivo_boton.seleccionado()
        self.iterativo_boton.deseleccionado()
        self.limpiar_valores()


    def obtener_datos(self):
        if self.contador < self.tamaño:
            self.contador += 1
            self.arreglo.append(int(self.campo.obtener_datos()))
            messagebox.showinfo("Atencion","Se agrego con exito")
            self.campo.limpiar_campo()

        else:
            messagebox.showinfo("Atencion","Se supero el limite del arreglo")
            self.campo.limpiar_campo()


    def iterativo(self):
        resultado = self.mensajero.iterativo(self.arreglo,int(self.campo2.obtener_datos()))
        self.area_texto.mostrar_texto_individual(resultado)
    def recursivo(self):
        resultado = self.mensajero.recursivo(self.arreglo,int(self.campo2.obtener_datos()))
        self.area_texto.mostrar_texto_individual(resultado)

    def opcion_seleccionada(self):
        if self.seleccion == "iterativo":
            self.iterativo()
        elif self.seleccion == "recursivo":
            self.recursivo()

    def limpiar_valores(self):
        self.area_texto.limpiar_area()