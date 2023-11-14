
class Euclides():

    def euclides_recursivo(self,a, b):
        if b == 0:
            return a
        else:
            return self.euclides_recursivo(b, a % b)

    def euclides_iterativo(self,a, b):
        while b != 0:
            a, b = b, a % b
        return a