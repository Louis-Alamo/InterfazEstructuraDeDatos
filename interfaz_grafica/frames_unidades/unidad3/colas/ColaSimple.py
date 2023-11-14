from numpy import zeros
from tkinter import messagebox
class ColaSimple():

    def __init__(self, n):
        self.n = n
        self.cola = zeros(self.n)
        self.frente = -1
        self.max = self.n
        self.final = -1

    def insertarElemento(self,dato):
            try:
                if self.final < self.max-1:
                    self.final += 1
                    self.cola[self.final] = dato
                    if self.final == 0:
                        self.frente = 0
                    messagebox.showinfo("","se inserto")
                else:
                    messagebox.showinfo("","Desboerdamiento-Cola llena")
            except IndexError:
                messagebox.showinfo("","Exception: indice fuera del limite, contacte con el desarrollador para posibles soluciones")

    def eliminarElemento(self):
        try:
            if self.frente != -1:
                dato = self.cola[self.frente]
                self.cola[self.frente] = None
                if self.frente == self.final:
                    self.frente = -1
                    self.final = -1
                else:
                    self.frente += 1
                messagebox.showinfo("", f"Se eliminó {dato} de la cola.")
            else:
                messagebox.showinfo("","Subdesbordamiento - Cola vacía")

        except IndexError:
            messagebox("","Indice fuera del limite, contacte con el desarrollador para posibles soluciones")

    def getCola(self):
        return self.cola

    def limpiar_valores(self):
        self.cola = zeros(self.n)
        self.frente = -1
        self.max = self.n
        self.final = -1
