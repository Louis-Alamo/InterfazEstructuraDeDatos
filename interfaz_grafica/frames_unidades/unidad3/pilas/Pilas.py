from numpy import array
from tkinter import messagebox

class Pila():

    def __init__(self, longitud):
        self.longitud = longitud
        self.tope = -1
        self.max = 0

        self.pila = array([None] * self.longitud)
        self.max = self.longitud

    def eliminarElemento(self):
        try:
            if self.comprobarPilaVacia(self.tope):
                messagebox.showwarning("Exception", "Subdesbordamiento -> Pila vacia")


            else:
                dato = self.pila[self.tope]
                self.pila[self.tope] = None
                self.tope -= 1

                messagebox.showinfo("","Dato eliminado")

        except IndexError:
            messagebox.showerror("Error!!!...","indice fuera de la pila revise el codigo del programa para solucionar el problema o contacte al desarrollador del software")


    def insertarElemento(self, dato):
        try:
            if self.comprobarPilaLlena(self.tope,self.max):
                messagebox.showwarning("Atención","Desbordamiento de la pila")

            else:
                self.tope += 1
                self.pila[self.tope] = dato
                messagebox.showinfo("Exito", "Elemento insertado")



        except IndexError:
            messagebox.showerror("Error!!!...", " indice fuera de la pila revise el codigo del programa para solucionar el problema o contacte al desarrollador del software")
        except ValueError:
            messagebox.showerror("Exception Value Error", "Solo se permite valores numericos")
            self.valorEntry.insert(0,"")

    def comprobarPilaLlena(self,tope,max):
        if tope == max-1:
            return True
        else:
            return False

    def comprobarPilaVacia(self, tope):
        if self.tope == -1:
            return True
        else:
            return False


    def getPila(self):
        return self.pila

    def limpiar_valores(self):
        self.tope = -1
        self.max = 0

        self.pila = array([None] * self.longitud)
        self.max = self.longitud
