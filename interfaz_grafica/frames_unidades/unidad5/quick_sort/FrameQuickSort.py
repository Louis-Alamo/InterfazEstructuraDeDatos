from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConBoton import CampoConBoton
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from interfaz_grafica.componentes_personalizados.botones.BotonPersonalizado import BotonPersonalizado
from interfaz_grafica.componentes_personalizados.componentes_multiples.CuadroInformacion import cuadroInformacion
from interfaz_grafica.frames_unidades.unidad5.quick_sort.QuickSort import QuickSort
from PIL import Image,ImageTk
from tkinter import messagebox,simpledialog, Frame

from numpy import *

class FrameQuickSort(FramePersonalizadoExtra):

    def __init__(self, master, titulo):
        super().__init__(master=master,titulo=titulo)
        self.seleccion = "mayor"
        self.comparaciones = 0
        self.movimientos = 0
        self.pasadas = 0
        self.comunicador = QuickSort()
        self.contadorUniversal = 0

        self.QuickSort_boton = BotonSeleccionManera(master=self, nombre_boton="QuickSort", nombre_funcion=self.QuickSort_funcion)
        self.QuickSort_boton.place(x=39, y=75)

        self.campo1 = CampoConBoton(master=self.canvas, titulo="Agregar elementos al arreglo", nombre_boton="Agregar",nombre_funcion=self.obtener_datos)
        self.lista_componentes.append(self.campo1)

        self.frame1 = Frame(self.canvas, bg="#FFFFFF")
        self.lista_componentes.append(self.frame1)


        self.elementos_agregados = AreaDeInformacion(master=self.frame1,titulo="Elementos agregados")
        self.elementos_agregados.pack(pady=10)

        self.boton_ordenar = BotonPersonalizado(master= self.frame1, funcion_boton=self.ordenar_datos, nombre_boton="Ordenar datos")
        self.boton_ordenar.configure(width=602, height=44)
        self.boton_ordenar.pack(pady=20)


        self.elementos_ordenados = AreaDeInformacion(master=self.canvas,titulo="Elementos ordenados")
        self.lista_componentes.append(self.elementos_ordenados)

        self.frame2 = Frame(self.canvas, bg="#FFFFFF")
        self.lista_componentes.append(self.frame2)


        #Creamos el cuadro informativo de moviminetos
        self.imagen_movimientos = Image.open("../imagenes/Movimientos.png")
        self.cuadro_movimientos = cuadroInformacion(master=self.frame2,imagen=self.imagen_movimientos,titulo="Movimientos", valor=self.movimientos)
        self.cuadro_movimientos.pack(side="left")

        self.imagen_comparaciones = Image.open("../imagenes/Comparaciones.png")
        self.cuadro_comparaciones = cuadroInformacion(master=self.frame2,imagen=self.imagen_comparaciones,titulo="Comparaciones", valor=self.comparaciones)
        self.cuadro_comparaciones.pack(side="left", padx=100)

        self.imagen_pasadas = Image.open("../imagenes/Pasadas.png")
        self.cuadro_pasadas = cuadroInformacion(master=self.frame2,imagen=self.imagen_movimientos,titulo="Pasadas", valor=self.pasadas)
        self.cuadro_pasadas.pack(side="left")

        self.agregar_lista_componentes(self.lista_componentes)

        self.tamaño = simpledialog.askinteger("Pregunta: ", "Cual es el tamaño de tu arreglo:")
        self.arreglo = zeros(self.tamaño)
        self.QuickSort_funcion()


    def QuickSort_funcion(self):
        print("Funciona mayor")
        self.QuickSort_boton.seleccionado()
        self.limpiar_valores()
    def volver(self):
        self.destroy()

    def obtener_datos(self):
        print(self.campo1.obtener_datos())
        messagebox.showinfo("exito", "Agregado correctamente")

    def obtener_datos(self):
        if self.contadorUniversal < self.tamaño:
            dato = int(self.campo1.obtener_datos())
            self.arreglo[self.contadorUniversal] = dato

            self.elementos_agregados.mostrar_informacion_estructura_numerica(self.arreglo)
            messagebox.showinfo("exito", "Agregado correctamente")
            self.contadorUniversal += 1
        else:
            messagebox.showinfo("Atencion", "No se pueden agregar ma selementos supera el limite")

        self.campo1.limpiar_campo()

    def ordenar_datos(self):
        print("entro")
        arreglo = self.arreglo.copy()
        self.pasadas, self.movimientos, self.comparaciones = self.comunicador.quicksort(arreglo)

        # self.cuadro_pasadas = lista[0]
        # self.cuadro_comparaciones = lista[1]
        # self.cuadro_movimientos = lista[2]
        self.actualizar_valores(arreglo)

    def actualizar_valores(self, arreglo):

        self.cuadro_pasadas.cambiar_valor(self.pasadas)
        self.cuadro_comparaciones.cambiar_valor(self.comparaciones)
        self.cuadro_movimientos.cambiar_valor(self.movimientos)
        self.elementos_ordenados.mostrar_informacion_estructura_numerica(arreglo)

    def limpiar_valores(self):
        self.pasadas = 0
        self.movimientos = 0
        self.comparaciones = 0
        self.cuadro_comparaciones.cambiar_valor(self.comparaciones)
        self.cuadro_movimientos.cambiar_valor(self.movimientos)
        self.cuadro_pasadas.cambiar_valor(self.pasadas)
        self.elementos_ordenados.mostrar_informacion_estructura_numerica(" ")