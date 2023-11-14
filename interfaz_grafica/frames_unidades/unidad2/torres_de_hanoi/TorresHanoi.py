
class TorresHanoi():

    def hanoi_iterativo(self,n, origen, destino, auxiliar):
        movimientos = []
        pila = [(n, origen, destino, auxiliar, False)]

        while pila:
            n, origen, destino, auxiliar, es_movimiento = pila.pop()

            if n == 1:
                movimientos.append(f"Mover disco 1 de {origen} a {destino}")
            elif not es_movimiento:
                pila.append((n, origen, destino, auxiliar, True))
                pila.append((n - 1, origen, auxiliar, destino, False))
            else:
                movimientos.append(f"Mover disco {n} de {origen} a {destino}")
                pila.append((n - 1, auxiliar, destino, origen, False))

        return movimientos

    def hanoi_recursivo(self,n, origen, destino, auxiliar, movimientos=None):
        if movimientos is None:
            movimientos = []

        if n == 1:
            movimientos.append(f"Mover disco 1 de {origen} a {destino}")
        else:
            self.hanoi_recursivo(n - 1, origen, auxiliar, destino, movimientos)
            movimientos.append(f"Mover disco {n} de {origen} a {destino}")
            self.hanoi_recursivo(n - 1, auxiliar, destino, origen, movimientos)

        return movimientos