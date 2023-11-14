def hanoi_iterativo(n, origen, destino, auxiliar):
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

# Ejemplo de uso
num_discos = 3
movimientos_iterativos = hanoi_iterativo(num_discos, 'A', 'C', 'B')
for i, movimiento in enumerate(movimientos_iterativos, start=1):
    print(f"{i}. {movimiento}")

# También puedes obtener todos los movimientos como una sola cadena
cadena_movimientos_iterativos = "\n".join(movimientos_iterativos)
print("\nMovimientos Iterativos:\n", cadena_movimientos_iterativos)
print(f"Total de movimientos: {len(movimientos_iterativos)}")
