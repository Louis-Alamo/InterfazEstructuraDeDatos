

class BusquedaBinaria():

    def iterativo(self,arr, objetivo):
        inicio = 0
        fin = len(arr) - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2

            if arr[medio] == objetivo:
                return f"El dato se encuentra en el arreglo, en la posicion: {medio}"
            elif arr[medio] < objetivo:
                inicio = medio + 1
            else:
                fin = medio - 1

        return "¡No encontré lo que buscabas, como era de esperar, maestro supremo de las preferencias!"

    def iterativo_bandera(self,arr, objetivo):
        inicio = 0
        fin = len(arr) - 1
        encontrado = False

        while inicio <= fin and not encontrado:
            medio = (inicio + fin) // 2

            if arr[medio] == objetivo:
                encontrado = True
            elif arr[medio] < objetivo:
                inicio = medio + 1
            else:
                fin = medio - 1

        return f"El dato se encuentra en la posicion: {medio}" if encontrado else "¡No encontré lo que buscabas, pero tu magnificencia no se ve afectada, oh exigente líder de las preferencias!"

    def recursivo(self,arr, objetivo, inicio=0, fin=None):
        if fin is None:
            fin = len(arr) - 1

        if inicio > fin:
            return "¡No encontré lo que buscabas, pero tu grandiosa petición no pasa desapercibida, oh infinito maestro de las preferencias!"

        medio = (inicio + fin) // 2

        if arr[medio] == objetivo:
            return f"El elemento se encuentra en la posicion: {medio}"
        elif arr[medio] < objetivo:
            return self.recursivo(arr, objetivo, medio + 1, fin)
        else:
            return self.recursivo(arr, objetivo, inicio, medio - 1)
