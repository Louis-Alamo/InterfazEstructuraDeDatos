
class Nodo():
    def __init__(self):
        self._valor = None
        self._liga = None

    def setValor(self, valor):
        self._valor = valor

    def setLiga(self, siguiente):
        self._liga = siguiente

    def getLiga(self):
        return self._liga

    def getValor(self):
        return self._valor