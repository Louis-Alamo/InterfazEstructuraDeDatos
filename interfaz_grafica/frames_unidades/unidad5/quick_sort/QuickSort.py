

class QuickSort:
    def quicksort(self, arr):
        pila = [(0, len(arr) - 1)]
        comparaciones = 0
        movimientos = 0
        pasadas = 0

        while pila:
            ini, fin = pila.pop()
            pasadas += 1
            pos, cmp, mov = self.particionar(arr, ini, fin)
            comparaciones += cmp
            movimientos += mov

            if ini < pos - 1:
                pila.append((ini, pos - 1))
            if fin > pos + 1:
                pila.append((pos + 1, fin))

        return pasadas, movimientos,comparaciones

    def particionar(self, arr, ini, fin):
        pivote = arr[ini]
        izquierda = ini + 1
        derecha = fin
        comparaciones = 0
        movimientos = 0

        hecho = False
        while not hecho:
            while izquierda <= derecha and arr[izquierda] <= pivote:
                izquierda += 1
                comparaciones += 1
            while arr[derecha] >= pivote and derecha >= izquierda:
                derecha -= 1
                comparaciones += 1
            if derecha < izquierda:
                hecho = True
            else:
                arr[izquierda], arr[derecha] = arr[derecha], arr[izquierda]
                movimientos += 1

        arr[ini], arr[derecha] = arr[derecha], arr[ini]
        movimientos += 1

        return derecha, comparaciones, movimientos