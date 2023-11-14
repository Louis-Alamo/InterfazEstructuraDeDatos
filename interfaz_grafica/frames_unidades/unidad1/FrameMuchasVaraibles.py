from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConTitulo import CampoConTitulo
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.componentes_personalizados.botones.BotonPersonalizado import BotonPersonalizado
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from tkinter import Frame
class FrameMuchasVaraibles(FramePersonalizadoExtra):

    def __init__(self, master, titulo):
        super().__init__(master = master, titulo=titulo)
        self.separacion = 100
        self.arreglo_boton = BotonSeleccionManera(master=self, nombre_boton="Con varaibles",
                                                        nombre_funcion=self.arreglo_funcion)
        self.arreglo_boton.place(x=39, y=75)


        self.campo1 = CampoConTitulo(self.canvas, titulo="Calificación 1")
        self.lista_componentes.append(self.campo1)

        self.campo2 = CampoConTitulo(self.canvas, titulo="Calificación 2")
        self.lista_componentes.append(self.campo2)

        self.campo3 = CampoConTitulo(self.canvas, titulo="Calificación 3")
        self.lista_componentes.append(self.campo3)

        self.campo4 = CampoConTitulo(self.canvas, titulo="Calificación 4")
        self.lista_componentes.append(self.campo4)

        self.campo5 = CampoConTitulo(self.canvas, titulo="Calificación 5")
        self.lista_componentes.append(self.campo5)

        self.boton_calcular = BotonPersonalizado(master=self.canvas, funcion_boton=self.arreglo_funcion_solver, nombre_boton="Calcular")
        self.lista_componentes.append(self.boton_calcular)

        self.area_texto = AreaDeInformacion(master=self.canvas, titulo="Resultado")
        self.lista_componentes.append(self.area_texto)

        self.agregar_lista_componentes(self.lista_componentes)

        self.arreglo_funcion()


    def arreglo_funcion(self):
        self.arreglo_boton.seleccionado()
        self.limpiar_valores()


    def arreglo_funcion_solver(self):
        cal1 = int(self.campo1.obtener_datos())
        cal2 = int(self.campo2.obtener_datos())
        cal3 = int(self.campo3.obtener_datos())
        cal4 = int(self.campo4.obtener_datos())
        cal5 = int(self.campo5.obtener_datos())

        suma = cal1 + cal2 + cal3 + cal4 + cal5
        promedio = suma / 5

        cont = 0
        if cal1 > promedio:
            cont += 1
        if cal2 > promedio:
            cont +=1
        if cal3 > promedio:
            cont += 1
        if cal4 > promedio:
            cont += 1
        if cal5 > promedio:
            cont += 1

        self.area_texto.mostrar_texto_concatenado(f"El promedio de las calificaciones es: {promedio}\nCalificaciones mayores al promedio: {cont}")


    def limpiar_valores(self):
        self.campo1.limpiar_campo()
        self.campo2.limpiar_campo()
        self.campo3.limpiar_campo()
        self.campo4.limpiar_campo()
        self.campo5.limpiar_campo()
        self.area_texto.limpiar_area()
