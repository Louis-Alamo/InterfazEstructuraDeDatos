

class ImprimirArregloDerechaIzquierda:

    def obtener_arreglo_iterativo_derecha_izquierda(self,arr):
        resultado = []
        for i in range(len(arr) - 1, -1, -1):
            resultado.append(arr[i])
        return resultado

    def obtener_arreglo_recursivo_derecha_izquierda(self,arr, indice=None, resultado=None):
        if resultado is None:
            resultado = []

        if indice is None:
            indice = len(arr) - 1

        if indice >= 0:
            resultado.append(arr[indice])
            self.obtener_arreglo_recursivo_derecha_izquierda(arr, indice - 1, resultado)

        return resultado
