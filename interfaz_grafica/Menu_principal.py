from tkinter import *
from PIL import Image, ImageTk
from interfaz_grafica.frames_unidades.unidad1.FrameUnidad1 import FrameUnidad1
from interfaz_grafica.frames_unidades.unidad2.FrameUnidad2 import FrameUnidad2
from interfaz_grafica.frames_unidades.unidad3.FrameUnidad3 import FrameUnidad3
from interfaz_grafica.frames_unidades.unidad4.FrameUnidad4 import FrameUnidad4
from interfaz_grafica.frames_unidades.unidad5.FrameUnidad5 import FrameUnidad5
from interfaz_grafica.componentes_personalizados.botones.BotonUnidad import BotonUnidad




class Menu_principal():

    def __init__(self):
        self.menu_ventana = Tk()
        self.menu_ventana.geometry("900x580")
        self.menu_ventana.title("Estructura de datos")
        self.menu_ventana.config(bg="#6053AF")


        #self.ultimo_frame = FrameUnidad1(self.menu_ventana)

        Label(self.menu_ventana, text="Estructura de \ndatos", font=("Inter", 18,"bold"), bg ="#6053AF", fg="#FFFFFF").place(x=16, y=28)

        self.boton_unidad1 = BotonUnidad(master=self.menu_ventana, nombre_boton="Unidad 1", nombre_funcion=self.unidad1_funcion)
        self.boton_unidad1.place(x=0,y=125)

        self.boton_unidad2 = BotonUnidad(master=self.menu_ventana, nombre_boton="Unidad 2", nombre_funcion=self.unidad2_funcion)
        self.boton_unidad2.place(x=0,y=175)

        self.boton_unidad3 = BotonUnidad(master=self.menu_ventana, nombre_boton="Unidad 3", nombre_funcion=self.unidad3_funcion)
        self.boton_unidad3.place(x=0,y=225)

        self.boton_unidad4 = BotonUnidad(master=self.menu_ventana, nombre_boton="Unidad 4", nombre_funcion=self.unidad4_funcion)
        self.boton_unidad4.place(x=0,y=275)

        self.boton_unidad5 = BotonUnidad(master=self.menu_ventana, nombre_boton="Unidad 5", nombre_funcion=self.unidad5_funcion)
        self.boton_unidad5.place(x=0,y=325)

        self.ultimo_boton = self.boton_unidad1
        self.ultimo_boton.seleccionado()

        self.unidad1_funcion()

        self.menu_ventana.mainloop()

    def redimensionar_imagen(self,imagen, nuevo_ancho, nuevo_alto):
        imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)
        return ImageTk.PhotoImage(imagen_redimensionada)

    def unidad1_funcion(self):
        self.ultimo_boton.deseleccionado()
        self.ultimo_boton = self.boton_unidad1
        self.ultimo_boton.seleccionado()

        self.frame = FrameUnidad1(self.menu_ventana)
        self.frame.place(x=194, y=11)

        self.ultimo_boton = self.boton_unidad1
        self.ultimo_boton.seleccionado()

    def unidad2_funcion(self):
        self.ultimo_boton.deseleccionado()
        self.ultimo_boton = self.boton_unidad2
        self.ultimo_boton.seleccionado()

        self.frame = FrameUnidad2(self.menu_ventana)
        self.frame.place(x=194, y=11)



    def unidad3_funcion(self):
        self.ultimo_boton.deseleccionado()
        self.ultimo_boton = self.boton_unidad3
        self.ultimo_boton.seleccionado()

        self.frame = FrameUnidad3(self.menu_ventana)
        self.frame.place(x=194, y=11)

    def unidad4_funcion(self):
        self.ultimo_boton.deseleccionado()
        self.ultimo_boton = self.boton_unidad4
        self.ultimo_boton.seleccionado()

        self.frame = FrameUnidad4(self.menu_ventana)
        self.frame.place(x=194, y=11)

    def unidad5_funcion(self):
        self.ultimo_boton.deseleccionado()
        self.ultimo_boton = self.boton_unidad5
        self.ultimo_boton.seleccionado()

        self.frame = FrameUnidad5(self.menu_ventana)
        self.frame.place(x=194, y=11)



Menu_principal()