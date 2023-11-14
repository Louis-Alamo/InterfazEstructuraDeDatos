from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConBoton import CampoConBoton
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from interfaz_grafica.componentes_personalizados.botones.BotonPersonalizado import BotonPersonalizado
from tkinter import messagebox
class FrameArreglos(FramePersonalizadoExtra):

    def __init__(self, master, titulo):
        super().__init__(master=master, titulo=titulo)
        self.arreglo = []
        self.contador = 0

        self.separacion = 100

        self.boton_seleccion = BotonSeleccionManera(master=self, nombre_boton="Con arreglos",
                                                        nombre_funcion=self.seleccion)
        self.boton_seleccion.place(x=39, y=75)

        self.campo = CampoConBoton(master=self.canvas, titulo="Ingresar numero", nombre_boton="Agregar", nombre_funcion=self.agregar)
        self.lista_componentes.append(self.campo)

        self.boton_realizar = BotonPersonalizado(master=self.canvas, funcion_boton=self.resolver, nombre_boton="Calcular")
        self.boton_realizar.configure(width=602)
        self.lista_componentes.append(self.boton_realizar)

        self.area_texto = AreaDeInformacion(master=master, titulo="Resultados: ")
        self.lista_componentes.append(self.area_texto)
        self.seleccion()

        self.agregar_lista_componentes(self.lista_componentes)


    def seleccion(self):
        self.boton_seleccion.seleccionado()
        self.limpiar_valores()

    def agregar(self):
        if self.contador < 5:
            self.arreglo.append(float(self.campo.obtener_datos()))
            self.contador += 1
            messagebox.showinfo("", "Agregado con exito")
            self.campo.limpiar_campo()
        else:
            messagebox.showinfo("", "Superas el limite de 5 en el arreglo")

    def resolver(self):
        promedio = 0
        for i in self.arreglo:
            promedio += i

        promedio = promedio / 5

        cont = 0
        for i in self.arreglo:
            if i > promedio:
                cont += 1

        self.area_texto.mostrar_texto_concatenado(texto=f"Promedio de las calificaciones: {promedio}\nCalificaciones que superaron al promedio: {cont}")


    def limpiar_valores(self):
        self.contador = 0
        self.arreglo = []
        self.campo.limpiar_campo()
        self.area_texto.limpiar_area()