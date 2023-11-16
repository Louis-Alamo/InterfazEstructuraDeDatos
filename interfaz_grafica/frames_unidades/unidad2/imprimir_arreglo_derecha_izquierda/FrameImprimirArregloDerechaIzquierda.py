from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConBoton import CampoConBoton
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.botones.BotonPersonalizado import BotonPersonalizado
from interfaz_grafica.frames_unidades.unidad2.imprimir_arreglo_derecha_izquierda.ImprimirArregloDerechaIzquierda import ImprimirArregloDerechaIzquierda
from tkinter import messagebox, simpledialog

from numpy import zeros



class FrameArregloDerechaIzquierda(FramePersonalizadoExtra):

    def __init__(self, master, titulo):
        super().__init__(master=master, titulo=titulo)
        self.seleccion = ""
        self.varaible = None
        self.separacion = 100
        self.comunicador = ImprimirArregloDerechaIzquierda()
        self.contador = 0
        self.boton_seleccion_iterativo = BotonSeleccionManera(master=self, nombre_boton="Iterativo", nombre_funcion=self.seleccion_manera_iterativo)
        self.boton_seleccion_iterativo.place(x=39,y=75)

        self.boton_seleccion_recursivo = BotonSeleccionManera(master=self, nombre_boton="Recursivo", nombre_funcion=self.seleccion_manera_recursivo)
        self.boton_seleccion_recursivo.place(x=189,y=75)


        self.campo_con_boton = CampoConBoton(master=self.canvas, titulo="Ingrese el dato", nombre_boton="Agregar", nombre_funcion=self.agregar_elemento)
        self.lista_componentes.append(self.campo_con_boton)

        self.calcular_boton = BotonPersonalizado(master=self.canvas, funcion_boton=self.realizar_impresiones, nombre_boton="Imprimir arreglo")
        self.calcular_boton.configure(width=602)
        self.lista_componentes.append(self.calcular_boton)

        self.area_texto = AreaDeInformacion(master=self.canvas, titulo="Resultado")
        self.lista_componentes.append(self.area_texto)

        self.agregar_lista_componentes(self.lista_componentes)


        self.tamaño = simpledialog.askinteger("Pregunta", "¿Cuantos valores quieres contener en el arreglo?")
        self.arreglo = zeros(self.tamaño)

        self.seleccion_manera_iterativo()


    def seleccion_manera_iterativo(self):
        self.seleccion = "iterativo"
        self.boton_seleccion_recursivo.deseleccionado()
        self.boton_seleccion_iterativo.seleccionado()
        self.limpiar_valores()

    def seleccion_manera_recursivo(self):
        self.seleccion = "recursivo"
        self.boton_seleccion_iterativo.deseleccionado()
        self.boton_seleccion_recursivo.seleccionado()
        self.limpiar_valores()
    def agregar_elemento(self):
        if self.contador < self.tamaño:
            self.arreglo[self.contador] = float(self.campo_con_boton.obtener_datos())
            self.contador += 1
            self.campo_con_boton.limpiar_campo()
            messagebox.showinfo("Exito", "Elemento agregado")
        else:
            messagebox.showinfo("titulo", "Superas el limite establecido del arreglo")
            self.campo_con_boton.limpiar_campo()


    def realizar_impresiones(self):
        resultado = []
        if self.seleccion == "iterativo":
            resultado = self.comunicador.obtener_arreglo_iterativo_derecha_izquierda(self.arreglo)
        elif self.seleccion == "recursivo":
            resultado = self.comunicador.obtener_arreglo_recursivo_derecha_izquierda(self.arreglo)

        self.area_texto.mostrar_informacion_estructura_numerica(resultado)


    def limpiar_valores(self):
        self.campo_con_boton.limpiar_campo()
        self.area_texto.mostrar_texto_individual("")
        self.varaible = ""
        for i in range(self.tamaño):
            self.arreglo[i] = 0

        self.contador=0


