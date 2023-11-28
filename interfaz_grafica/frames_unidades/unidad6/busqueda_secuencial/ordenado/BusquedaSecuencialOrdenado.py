class BusquedaSecuencialOrdenado():

    def iterativo(self,arreglo, elemento):
        for i in range(len(arreglo)):
            if arreglo[i] == elemento:
                return f"Encontrado en la posición {i}"
            elif arreglo[i] > elemento:
                return "Elemento no encontrado"
        return "Elemento no encontrado"

    def recursivo(self,arreglo, elemento, inicio=0, fin=None):
        if fin is None:
            fin = len(arreglo) - 1

        if inicio > fin:
            return "Elemento no encontrado"

        if arreglo[inicio] == elemento:
            return f"Encontrado en la posición {inicio}"
        elif arreglo[inicio] > elemento:
            return "Elemento no encontrado"
        else:
            return self.recursivo(arreglo, elemento, inicio + 1, fin)


