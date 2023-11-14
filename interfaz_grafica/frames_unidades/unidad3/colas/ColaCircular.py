from numpy import zeros
from tkinter import messagebox
class ColaCircular():

    def __init__(self, n):
        self.n = n
        self.cola = zeros(self.n)
        self.frente = -1
        self.max = n
        self.final = -1

    def insertarElemento(self,dato):
        try:
            if (self.final + 1 == self.frente) or (self.frente == 0 and self.final == self.max - 1):
                messagebox.showinfo("","Desbordamiento - Cola llena")
            else:
                if self.frente == -1:
                    self.frente = 0
                    self.final = 0
                else:
                    if self.final == self.max - 1:
                        self.final = 0
                    else:
                        self.final += 1
                self.cola[self.final] = dato
                messagebox.showinfo("", "Se inserto")


        except IndexError:
            messagebox.showinfo("","Exception: Indice fuera del limite")

    def eliminarElemento(self,):
        if self.frente == -1:
            messagebox.showinfo("", "Subdesbordamiento - Cola vacía")
        else:
            dato = self.cola[self.frente]
            self.cola[self.frente] = None
            messagebox.showinfo("",f"Se elimino el dato")

            if self.frente == self.final:
                self.frente = -1
                self.final = -1
            elif self.frente == self.max - 1:
                self.frente = 0
            else:
                self.frente += 1

    def getCola(self):
        return self.cola
    def limpiar_valores(self):
        self.cola = zeros(self.n)
        self.frente = -1
        self.max = self.n
        self.final = -1
