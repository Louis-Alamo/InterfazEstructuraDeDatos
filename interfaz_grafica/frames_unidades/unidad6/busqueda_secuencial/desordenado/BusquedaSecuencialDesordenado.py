
class BusquedaSecuencialDesordenado():

    def recursivo(self, arreglo, tamaño, elemento, cont):
        if cont >= tamaño:
            return "La información no se encuentra en el arreglo"
        else:
            if arreglo[cont] == elemento:
                return f"La información se encuentra en la posición: {cont}"
            else:
                return self.recursivo(arreglo, tamaño, elemento, cont + 1)

    def iterativo(self, elemento, arreglo):

        for i in range(len(arreglo)):
            if arreglo[i] == elemento:
                return f"La informacion se encuentra en el arreglo, en la posicion: {i}"

        return f"La informacion no se encuentra en el arreglo"
