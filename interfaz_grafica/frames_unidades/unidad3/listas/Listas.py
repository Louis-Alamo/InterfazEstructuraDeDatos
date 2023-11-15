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
    def recorrer_recursivo(self):
        datos = []
        self.recorrer_recursivo_aux(self.nodo, datos)
        return datos
    def recorrer_recursivo_aux(self, nodo, datos):
        if nodo is not None:
            datos.append(str(nodo.getValor()) + " → " )
            self.recorrer_recursivo_aux(nodo.getLiga(), datos)


    def insertar_inicio(self, dato):
        if self.banderaCreacion == False:
            messagebox.showwarning("Atencion","No hay listas creadas, por lo que tiene que crear una primero")
        else:
            nodoQ = Nodo()
            nodoQ.setValor(dato)
            nodoQ.setLiga(self.nodo)
            self.nodo = nodoQ
            messagebox.showinfo("Exito", f"Se inserto el elemento {dato} en la lista")

    def insertar_final(self,dato):
        if self.banderaCreacion == False:
            messagebox.showwarning("Atencion","No hay listas creadas, por lo que tiene que crear una primero")

        else:
            nodoT = self.nodo
            while nodoT.getLiga() != None:
                nodoT = nodoT.getLiga()

            nodoQ = Nodo()
            nodoQ.setValor(dato)
            nodoQ.setLiga(None)
            nodoT.setLiga(nodoQ)
            messagebox.showinfo("Exito", f"Se inserto el dato {dato} en la lista")

    def insertar_antes_de(self, valorAlmacenar, datoReferencia):
        if self.banderaCreacion:
            nodoQ = self.nodo
            nodoT = None
            bandera = 1

            while nodoQ.getValor() != datoReferencia and bandera == 1:
                if nodoQ.getLiga() is not None:
                    nodoT = nodoQ
                    nodoQ = nodoQ.getLiga()
                else:
                    bandera = 0

            if bandera == 1:
                nodoX = Nodo()
                nodoX.setValor(valorAlmacenar)

                if nodoT is None:
                    # Si el nodo de referencia es el primer nodo de la lista
                    nodoX.setLiga(self.nodo)
                    self.nodo = nodoX
                    messagebox.showinfo("Exito", f"El dato {valorAlmacenar} ha sido insertado correctamente")
                else:
                    # Si el nodo de referencia no es el primer nodo
                    nodoT.setLiga(nodoX)
                    nodoX.setLiga(nodoQ)
                    messagebox.showinfo("Exito", f"El dato {valorAlmacenar} ha sido insertado correctamente")

            else:
                messagebox.showinfo("","Sin exito", "El dato como referencia no se encuetra en la lista")
        else:
            messagebox.showwarning("Atencion", "No hay una lista creada, por lo que debera crear una")

    def insertar_despues_de(self, valorAlmacenar, valorReferencia):
        if self.banderaCreacion:
            nodoQ = self.nodo
            bandera = 1

            while nodoQ.getValor() != valorReferencia and bandera == 1:
                if nodoQ.getLiga() != None:
                    nodoQ = nodoQ.getLiga()

                else:
                    bandera == 0

            if bandera == 1:
                nodoT = Nodo()
                nodoT.setValor(valorAlmacenar)
                nodoT.setLiga(nodoQ.getLiga())
                nodoQ.setLiga(nodoT)
                messagebox.showinfo("Exito", f"El dato {valorAlmacenar} fue insertado correctamente")

            else:
                messagebox.showinfo("Sin exito",
                                    f"El dato {valorReferencia} dado como referencia no sse encuentra en la lista")
        else:
            messagebox.showwarning("Atencion", "No hay listas creadas, por lo que tiene que crear una")


    def eliminar_inicio(self):
        if self.banderaCreacion:
            nodoQ = self.nodo
            self.nodo = nodoQ.getLiga()
            messagebox.showinfo("Exito", "Dato eliminado")
            if self.nodo == None:
                self.banderaCreacion = False
                messagebox.showwarning("Atencion", "Elimino el ultimo valor de la lista por lo que tendra que crearla de nuevo")
        else:
            messagebox.showinfo("Atencion", "No hay listas existentes, por lo que tendra que crear una")
    def eliminar_final(self):
        if self.banderaCreacion:
            if self.nodo is None:
                messagebox.showwarning("Atencion", "La lsita esta vacia por lo que no contiene ningun dato")
            elif self.nodo.getLiga() is None:
                # Si hay solo un nodo en la lista
                self.nodo = None
                messagebox.showinfo("Elemento eliminado")
            else:
                nodoQ = self.nodo
                nodoT = None
                while nodoQ.getLiga() is not None:
                    nodoT = nodoQ
                    nodoQ = nodoQ.getLiga()
                nodoT.setLiga(None)
                messagebox.showinfo("Exito", "Elemento eliminado")
        else:
            messagebox.showwarning("Atencion","No hay listas creadasd por lo que tendras que crear una ")
    def elimina_nodo_x(self, valorX):
        if self.banderaCreacion:
            nodoQ = self.nodo
            nodoT = None
            bandera = 1

            while nodoQ is not None and nodoQ.getValor() != valorX and bandera == 1:
                if nodoQ.getLiga() is not None:
                    nodoT = nodoQ
                    nodoQ = nodoQ.getLiga()
                else:
                    bandera = 0

            if bandera == 0:
                messagebox.showinfo("Sin exito", "El elemento no se encuentra en la lista ")
            else:
                if nodoT is None:
                    # Si el nodo a eliminar es el primer nodo de la lista
                    self.nodo = nodoQ.getLiga()
                    messagebox.showinfo("Exito", "Elemento eliminado")
                else:
                    # Si el nodo a eliminar no es el primer nodo
                    nodoT.setLiga(nodoQ.getLiga())
                    messagebox.showinfo("Exito", "Elemento eliminado")
        else:
            messagebox.showwarning("Atencion", "No se han creado una lista por lo que debe crear una")
    def elimina_despues_de(self,valor_referencia):
        if self.banderaCreacion:
            nodoQ = self.nodo
            bandera = 1

            while nodoQ is not None and nodoQ.getValor() != valor_referencia and bandera == 1:
                if nodoQ.getLiga() is not None:
                    nodoQ = nodoQ.getLiga()
                else:
                    bandera = 0

            if bandera == 0 or nodoQ.getLiga() is None:
                messagebox.showinfo("Sin exito", "No se puede eliminar el nodo que sigue al dato de referencia")
            else:
                nodo_eliminar = nodoQ.getLiga()
                nodoQ.setLiga(nodo_eliminar.getLiga())
                nodo_eliminar = None
                messagebox.showinfo("Exito", "Elemento eliminado")
        else:
            messagebox.showwarning("Atencion", "Necesita crear una lista antes")
    def elimina_antes_de(self,valorX):
        if self.banderaCreacion:
            nodoQ = None
            nodoT = None
            nodoR = None
            if self.nodo.getValor() == valorX:
                messagebox.showinfo("Sin exito", "No hay un valor que preceda del dato de referencia")
            else:
                nodoQ = self.nodo
                nodoT = self.nodo
                bandera = 1

                while nodoQ.getValor() != valorX and bandera == 1:
                    if nodoQ.getLiga() != None:
                        nodoR = nodoT
                        nodoT = nodoQ
                        nodoQ = nodoQ.getLiga()
                    else:
                        bandera = 0

                if bandera == 0:
                    messagebox.showinfo("Sin exito", "El valor dado como referencia no se encuentra en la lista")
                else:
                    if self.nodo.getLiga() == nodoQ:
                        self.nodo = nodoQ
                        messagebox.showinfo("Exito", "Elemento eliminado")
                    else:
                        nodoR.setLiga(nodoQ)
                        messagebox.showinfo("Exito", "Elemento eliminado")
        else:
            messagebox.showwarning("Atencion", "No hay una lista creada por lo que tiene que crear una")

    def busqueda_ordenada(self, valor_buscar):
        if self.banderaCreacion:
            # Solo funciona con valores ordenados
            nodoQ = self.nodo

            while nodoQ is not None and nodoQ.getValor() < valor_buscar:
                nodoQ = nodoQ.getLiga()

            if nodoQ is None or nodoQ.getValor() > valor_buscar:
                messagebox.showinfo("Sin exito", "EL elemento no se encuentra en la lista")

            else:
                messagebox.showinfo("Exito", "El elemento se encuentra en la lista")
        else:
            messagebox.showwarning("Atencion", "No hay listas creadas por lo que tendra que crear una")

    def busqueda_desordenada(self, valorBuscar):
        if self.banderaCreacion:
            nodoQ = self.nodo
            while nodoQ != None and nodoQ.getValor() != valorBuscar:
                nodoQ = nodoQ.getLiga()

            if nodoQ == None:
                messagebox.showinfo("Sin exito", "El elemento no se encuentra en la lista")
            else:
                messagebox.showinfo("Exito", "El elemetno si se encuentra en la lista")
        else:
            messagebox.showwarning("Atencion", "No existe ninguna lista por lo que tendra que crear una")

    def busqueda_recursivas(self, nodo=None, valor_buscar=None):
        if nodo is None:
            messagebox.showinfo("SIn exito", "El elemento no se encuentra en la lista")
            return
        if nodo.getValor() == valor_buscar:
            messagebox.showinfo("Exito", "El elemento si se encuentra en la lista")
            return
        self.busqueda_recursivas(nodo.getLiga(), valor_buscar)

    def getBanderaCreacion(self):
        return self.banderaCreacion

    def reiniciar_valores(self):
        self.banderaCreacion = False
