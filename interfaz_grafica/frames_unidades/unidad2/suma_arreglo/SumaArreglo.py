

class SumaArreglo():

    def suma_iterativa(self,arr):
        suma = 0
        for elemento in arr:
            suma += elemento
        return suma

    def suma_recursiva(self,arr, indice=0):
        if indice == len(arr):
            return 0
        else:
            return arr[indice] + self.suma_recursiva(arr, indice + 1)