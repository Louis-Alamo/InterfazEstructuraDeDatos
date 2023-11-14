class Burbuja():
    def burbuja_mayor(self, arreglo):
        contComparaciones = 0
        contMovimientos = 0
        contadorPasadas = 0
        for i in range(len(arreglo)):
            for j in range(len(arreglo) - 1, i, -1):
                contComparaciones += 1
                if arreglo[j] < arreglo[j - 1]:
                    auxiliar = arreglo[j]
                    arreglo[j] = arreglo[j - 1]
                    arreglo[j - 1] = auxiliar
                    contMovimientos += 1

            contadorPasadas += 1
        print(contadorPasadas)
        print(contMovimientos)
        print(contComparaciones)
        return [contadorPasadas, contMovimientos, contComparaciones]




    def burbuja_menor(self, arreglo):
        contComparaciones = 0
        contMovimientos = 0
        contadorPasadas = 0

        for i in range(len(arreglo) - 1):
            for j in range(len(arreglo) - 1 - i):
                contComparaciones += 1
                if arreglo[j] > arreglo[j + 1]:
                    auxiliar = arreglo[j]
                    arreglo[j] = arreglo[j + 1]
                    arreglo[j + 1] = auxiliar
                    contMovimientos += 1
            contadorPasadas += 1
        return [contadorPasadas, contMovimientos, contComparaciones]


    def burbuja_señal(self, arreglo):
        i = 0
        bandera = False
        aux = None
        contMovimientos = 0
        contComparaciones = 0
        while (i <= len(arreglo)-1) and bandera == False:
            bandera = True
            for j in range(0,len(arreglo)-1):
                contComparaciones += 1
                if arreglo[j] > arreglo[j+1]:
                    aux = arreglo[j]
                    arreglo[j] = arreglo[j+1]
                    arreglo[j+1] = aux
                    bandera = False
                    contMovimientos += 1
            i +=1
        return [i, contMovimientos, contComparaciones]

