

class ImprimirArregloIzquierdaDerecha:

    def obtener_arreglo_iterativo(self,arr):
        resultado = []
        for elemento in arr:
            resultado.append(elemento)
        return resultado

    def obtener_arreglo_recursivo(self,arr, indice=0, resultado=None):
        if resultado is None:
            resultado = []

        if indice < len(arr):
            resultado.append(arr[indice])
            self.obtener_arreglo_recursivo(arr, indice + 1, resultado)

        return resultado