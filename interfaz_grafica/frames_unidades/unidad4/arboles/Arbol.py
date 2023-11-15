from tkinter import messagebox
from interfaz_grafica.frames_unidades.unidad4.arboles.Nodo import Nodo

class Arbol:

    def __init__(self):
        self.banderaCreacion = False
        self.arbol = None

    def crear_arbol(self, valor):
        self.arbol = Nodo(valor)
        messagebox.showinfo("Árbol Creado", f"Árbol creado exitosamente con nodo raíz: {valor}")
        self.banderaCreacion = True

    def recorrer_inorden(self):
        lista_resultado = []

        def recorrer_aux(nodo):
            if nodo:
                recorrer_aux(nodo.izquierda)
                lista_resultado.append(str(nodo.info) + "  ")
                recorrer_aux(nodo.derecha)

        recorrer_aux(self.arbol)
        return lista_resultado

    def recorrer_posorden(self):
        lista_resultado = []

        def recorrer_aux(nodo):
            if nodo:
                recorrer_aux(nodo.izquierda)
                recorrer_aux(nodo.derecha)
                lista_resultado.append(str(nodo.info) + "  ")

        recorrer_aux(self.arbol)
        return lista_resultado

    def recorrer_preorden(self):
        lista_resultado = []

        def recorrer_aux(nodo):
            if nodo:
                lista_resultado.append(str(nodo.info) + "  ")
                recorrer_aux(nodo.izquierda)
                recorrer_aux(nodo.derecha)

        recorrer_aux(self.arbol)
        return lista_resultado

    def buscar_elemento(self, dato):
        def busqueda(apnodo, informacion):
            if apnodo != None:
                if informacion < apnodo.info:
                    busqueda(apnodo.izquierda, informacion)
                else:
                    if informacion > apnodo.info:
                        busqueda(apnodo.derecha, informacion)
                    else:
                        messagebox.showinfo("","La informacion se encuetra en el arbol")
            else:
                messagebox.showinfo("","La informacion no se encuentra en el arbol")

        busqueda(apnodo=self.arbol,informacion=dato)


    def insertar_elemento(self,dato):
        bandera = False
        def insertar(apnodo, informacion):
            if apnodo is None:
                return Nodo(informacion)
            if informacion < apnodo.info:
                apnodo.izquierda = insertar(apnodo.izquierda, informacion)
            elif informacion > apnodo.info:
                apnodo.derecha = insertar(apnodo.derecha, informacion)
            else:
                messagebox.showinfo("","La información ya se encuentra en el árbol")
                bandera = True
            return apnodo

        insertar(self.arbol,dato)
        if bandera != True:
            messagebox.showinfo("", "Se inserto el dato en el arbol")

    def eliminar_elemento(self,dato):
        def eliminar( apnodo, informacion):
            if apnodo is None:
                print("La información a eliminar no se encuentra en el árbol")
                return apnodo

            # Buscar el nodo a eliminar en el subárbol izquierdo
            if informacion < apnodo.info:
                apnodo.izquierda = eliminar(apnodo.izquierda, informacion)
            # Buscar el nodo a eliminar en el subárbol derecho
            elif informacion > apnodo.info:
                apnodo.derecha = eliminar(apnodo.derecha, informacion)
            # Nodo encontrado, proceder con la eliminación
            else:
                # Caso 1: Nodo sin hijos o con un solo hijo
                if apnodo.izquierda is None:
                    temp = apnodo.derecha
                    apnodo = None
                    return temp
                elif apnodo.derecha is None:
                    temp = apnodo.izquierda
                    apnodo = None
                    return temp

                # Caso 2: Nodo con dos hijos, encontrar el sucesor inorden en el subárbol derecho
                temp = self.encontrar_minimo(apnodo.derecha)

                # Copiar el contenido del sucesor inorden al nodo actual
                apnodo.info = temp.info

                # Eliminar el sucesor inorden del subárbol derecho
                apnodo.derecha = eliminar(apnodo.derecha, temp.info)

            return apnodo

        eliminar(self.arbol, dato)

    def encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def getBanderaCreacion(self):
        return self.banderaCreacion



