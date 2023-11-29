class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        # Manejo de colisiones por reasignación (sondeo lineal)
        while self.table[index] is not None:
            # Incrementar el índice de manera lineal
            index = (index + 1) % self.size

        # Insertar el valor en la posición encontrada
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)

        # Buscar el valor en la posición calculada y en posiciones posteriores si es necesario
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]  # Devuelve el valor asociado a la clave
            # Incrementar el índice de manera lineal
            index = (index + 1) % self.size

        return None  # Clave no encontrada
