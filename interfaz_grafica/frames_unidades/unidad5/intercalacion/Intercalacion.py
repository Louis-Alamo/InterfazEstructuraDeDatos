
import time

class Intercalacion:
    def __init__(self, nombre_archivo1, nombre_archivo2, nombre_archivo_resultante):
        self.F1 = nombre_archivo1
        self.F2 = nombre_archivo2
        self.F3 = nombre_archivo_resultante
        self.log_text = ""

    def log(self, mensaje):
        self.log_text += mensaje + '\n'

    def ordenar_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'r') as file:
            lines = sorted([line.strip() for line in file], key=int)
        with open(nombre_archivo, 'w') as file:
            for line in lines:
                file.write(line + '\n')
                self.log(f'Escribiendo en {nombre_archivo} después de ordenar: {line}')

    def intercalacion(self):
        with open(self.F1, 'r') as file1, open(self.F2, 'r') as file2, open(self.F3, 'w') as file3:
            R1 = file1.readline().strip()
            R2 = file2.readline().strip()

            while R1 and R2:
                if int(R1) < int(R2):
                    file3.write(R1 + '\n')
                    self.log(f'Escribiendo en {self.F3} después de intercalar: {R1}')
                    R1 = file1.readline().strip()
                else:
                    file3.write(R2 + '\n')
                    self.log(f'Escribiendo en {self.F3} después de intercalar: {R2}')
                    R2 = file2.readline().strip()

            while R1:
                file3.write(R1 + '\n')
                self.log(f'Escribiendo en {self.F3} después de intercalar: {R1}')
                R1 = file1.readline().strip()

            while R2:
                file3.write(R2 + '\n')
                self.log(f'Escribiendo en {self.F3} después de intercalar: {R2}')
                R2 = file2.readline().strip()

    def inicioAlgoritmo(self):
        # Ordenar los archivos F1 y F2
        self.log(f"Ordenando archivos {self.F1} y {self.F2}...")
        start_time = time.time()
        self.ordenar_archivo(self.F1)
        self.ordenar_archivo(self.F2)
        end_time = time.time()
        self.log(f"Ordenación de archivos tomó {end_time - start_time:.6f} segundos")

        # Ejecutar el algoritmo de intercalación
        start_time = time.time()
        self.intercalacion()
        end_time = time.time()
        self.log(f"Intercalación tomó {end_time - start_time:.6f} segundos")

        # Mostrar contenido del archivo resultante F3
        self.log("\nContenido del archivo F3 después de la intercalación:")
        with open(self.F3, "r") as f3:
            self.log(f3.read())

    def get_log(self):
        return self.log_text