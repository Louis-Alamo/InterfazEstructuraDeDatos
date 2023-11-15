from interfaz_grafica.frames_unidades.unidad3.listas.Nodo import Nodo
from tkinter import messagebox
class Listas():

    def __init__(self):
        self.nodo = Nodo()
        self.datos = ""
        self.banderaCreacion = False

    def crear_lista(self,dato):
        self.nodo = Nodo()
        liga = None
        self.nodo.setValor(dato)
        self.nodo.setLiga(liga)

        self.banderaCreacion = True
        messagebox.showinfo("Exito", f"Se agrego el inicio con el dato {dato} a la lista")

    def recorrer_iterativo(self):
        nodoQ = self.nodo
        dato = ""

        while nodoQ is not None:
            dato += str(nodoQ.getValor()) + " → "
            nodoQ = nodoQ.getLiga()

        # Eliminar el último " → " agregado
        dato = dato.rstrip(" → ")

        return dato

    def recorrer_recursivo(self, nodo=None, datos=None):
        print("Entro recursivo")
        if datos is None:
            # Inicializa la lista de datos si no se proporciona
            datos = []

        if self.nodo is not None:
            # Agrega el valor del nodo a la lista de datos
            datos.append(self.nodo.getValor())
            print(self.nodo.getValor())
            # Llamada recursiva para el siguiente nodo
            self.recorrer_recursivo(self.nodo.getLiga(), datos)

        return datos

    def getBanderaCreacion(self):
        return self.banderaCreacion

    def reiniciar_valores(self):
        self.banderaCreacion = False
