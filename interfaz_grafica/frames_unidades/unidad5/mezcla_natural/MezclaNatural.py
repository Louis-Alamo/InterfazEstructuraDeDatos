class MezclaNatural:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def identificar_series(self):
        with open(self.nombre_archivo, 'r') as archivo:
            series = []
            serie_actual = [int(archivo.readline().strip())]

            for linea in archivo:
                num_actual = int(linea.strip())

                if num_actual >= serie_actual[-1]:
                    serie_actual.append(num_actual)
                else:
                    series.append(serie_actual)
                    serie_actual = [num_actual]

            if serie_actual:
                series.append(serie_actual)

        return series

    def fusionar_series(self, series):
        with open(self.nombre_archivo, 'w') as archivo:
            for serie in series:
                archivo.write('\n'.join(map(str, serie)) + '\n')

    def mezcla_final(self):
        series = self.identificar_series()

        while len(series) > 1:
            nueva_serie = []
            for i in range(0, len(series), 2):
                if i + 1 < len(series):
                    nueva_serie.extend(self.mezclar(series[i], series[i + 1]))
                else:
                    nueva_serie.extend(series[i])

            series = [nueva_serie]

        self.fusionar_series(series)

    def mezclar(self, serie1, serie2):
        resultado = []
        idx1 = idx2 = 0

        while idx1 < len(serie1) and idx2 < len(serie2):
            if serie1[idx1] <= serie2[idx2]:
                resultado.append(serie1[idx1])
                idx1 += 1
            else:
                resultado.append(serie2[idx2])
                idx2 += 1

        resultado.extend(serie1[idx1:])
        resultado.extend(serie2[idx2:])

        return resultado

    def inicio_algoritmo(self):
        self.mezcla_final()