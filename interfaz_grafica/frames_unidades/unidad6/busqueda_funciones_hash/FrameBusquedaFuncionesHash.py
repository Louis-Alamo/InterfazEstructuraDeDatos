from interfaz_grafica.componentes_personalizados.frames.FramePersonalizadoExtra import FramePersonalizadoExtra
from interfaz_grafica.componentes_personalizados.componentes_multiples.CampoConTitulo import CampoConTitulo
from interfaz_grafica.componentes_personalizados.botones.BotonPersonalizado import BotonPersonalizado
from interfaz_grafica.componentes_personalizados.botones.BotonSeleccionManera import BotonSeleccionManera
from interfaz_grafica.frames_unidades.unidad6.busqueda_funciones_hash.BusquedaFuncionesHash import HashTable
from interfaz_grafica.componentes_personalizados.componentes_multiples.AreaDeInformacion import AreaDeInformacion
from tkinter import simpledialog, Frame, messagebox
class FrameBusquedaFuncionesHash(FramePersonalizadoExtra):


    def __init__(self, master, titulo):
        super().__init__(master=master, titulo=titulo)
        self.separacion = 100

        self.Pordivision = BotonSeleccionManera(master=self, nombre_boton="Por division",nombre_funcion=self.seleccion_division)
        self.Pordivision.place(x=39, y=75)

        self.campo_valor = CampoConTitulo(master=self.canvas, titulo="Ingresa el valor")
        self.campo_valor.configure(width=602)
        self.campo_valor.campo.configure(width=600)
        self.lista_componentes.append(self.campo_valor)

        self.campo_clave = CampoConTitulo(master=self.canvas, titulo="Ingresa la clave")
        self.campo_clave.configure(width=602)
        self.campo_clave.campo.configure(width=600)
        self.lista_componentes.append(self.campo_clave)

        self.frame = Frame(master=self.canvas, width=663, bg="#FFFFFF")
        self.lista_componentes.append(self.frame)

        self.agregar = BotonPersonalizado(master=self.frame, funcion_boton=self.agregar_datos, nombre_boton="Agregar")
        self.agregar.pack(side="left", padx=10)
        #self.lista_componentes.append(self.agregar)

        self.buscar = BotonPersonalizado(master=self.frame, funcion_boton=self.buscar_dato, nombre_boton="Buscar dato")
        self.buscar.pack(side="right", padx=10)
        #self.lista_componentes.append(self.buscar)

        self.area_texto = AreaDeInformacion(master=self.canvas, titulo="Resultado")
        self.lista_componentes.append(self.area_texto)




        self.tamaño = simpledialog.askinteger("Atencion", "Dame el tamaño de tu diccionario")
        self.comunicador = HashTable(self.tamaño)
        self.contador = 0
        self.seleccion_division()

        self.agregar_lista_componentes(self.lista_componentes)


    def seleccion_division(self):
        self.Pordivision.seleccionado()

    def agregar_datos(self):
        if self.contador < self.tamaño:
            valor = int(self.campo_valor.obtener_datos())
            clave = int(self.campo_clave.obtener_datos())
            self.comunicador.insert(clave, valor)
            self.contador +=1
            self.campo_valor.limpiar_campo()
            self.campo_clave.limpiar_campo()
            messagebox.showinfo("Atencion", "Se agrego correctamente")

    def buscar_dato(self):
        clave = int(self.campo_clave.obtener_datos())
        resultado = self.comunicador.search(clave)
        if resultado != None:
            self.area_texto.mostrar_texto_individual(f"El valor asociado a la clave {clave} es: {resultado}")
        else:
            self.area_texto.mostrar_texto_individual(f"No hay ningun valor asociado a la clave {clave}")
