import random
import time

class MezclaDirecta:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.informacion = "Informacion del proceso:\n"  # Variable para almacenar la información
        self.tiempo = 0
    def generar_archivo_aleatorio(self, tamaño):
        with open(self.ruta_archivo, 'w') as f:
            datos = [random.randint(1, 1000) for _ in range(tamaño)]
            f.write(' '.join(map(str, datos)))

    def obtener_informacion(self):
        return self.informacion

    def agregar_informacion(self, texto):
        self.informacion += texto + '\n'  # Agregar el texto con un salto de línea al final

    def mezcla_directa(self):
        tiempo_inicio = time.time()

        # Leer datos del archivo
        with open(self.ruta_archivo, 'r') as f:
            datos = list(map(int, f.read().split()))

        n = len(datos)
        parte = 1

        self.agregar_informacion(f"Iniciando ordenamiento con {n} elementos")

        while parte < n:
            self.agregar_informacion(f"Particionando y fusionando con PART = {parte}")
            self.particion('F1.txt', 'F2.txt', parte)
            self.fusionar('F1.txt', 'F2.txt', parte)
            parte *= 2

        tiempo_fin = time.time()
        tiempo_transcurrido = tiempo_fin - tiempo_inicio
        self.agregar_informacion(f"\nTiempo transcurrido: {tiempo_transcurrido}")
        self.tiempo = tiempo_transcurrido

        self.agregar_informacion("\nDatos finales del archivo1:")
        with open('F1.txt', 'r') as f1:
            self.agregar_informacion(f1.read())

        self.agregar_informacion("\nDatos finales del archivo2:")
        with open('F2.txt', 'r') as f2:
            self.agregar_informacion(f2.read())

        self.agregar_informacion("\nDatos finales del archivo original ordenados:")
        with open('F3.txt', 'r') as f3:
            self.agregar_informacion(f3.read())

    def particion(self, ruta_f1, ruta_f2, parte):
        with open(self.ruta_archivo, 'r') as f:
            datos = list(map(int, f.read().split()))

        n = len(datos)

        with open(ruta_f1, 'w') as f1, open(ruta_f2, 'w') as f2:
            for i in range(0, n, parte * 2):
                f1.write(' '.join(map(str, datos[i:i + parte])) + '\n')
                f2.write(' '.join(map(str, datos[i + parte:i + 2 * parte])) + '\n')

    def fusionar(self, ruta_f1, ruta_f2, parte):
        with open(self.ruta_archivo, 'w') as f, open(ruta_f1, 'r') as f1, open(ruta_f2, 'r') as f2:
            r1 = f1.readline().strip().split()
            r2 = f2.readline().strip().split()

            while r1 and r2:
                i = j = 0

                while i < len(r1) and j < len(r2):
                    if int(r1[i]) <= int(r2[j]):
                        f.write(r1[i] + ' ')
                        i += 1
                    else:
                        f.write(r2[j] + ' ')
                        j += 1

                while i < len(r1):
                    f.write(r1[i] + ' ')
                    i += 1

                while j < len(r2):
                    f.write(r2[j] + ' ')
                    j += 1

                f.write('\n')
                r1 = f1.readline().strip().split()
                r2 = f2.readline().strip().split()

            # Agregar el contenido restante de F1 y F2
            while r1:
                f.write(' '.join(r1) + ' ')
                r1 = f1.readline().strip().split()

            while r2:
                f.write(' '.join(r2) + ' ')
                r2 = f2.readline().strip().split()