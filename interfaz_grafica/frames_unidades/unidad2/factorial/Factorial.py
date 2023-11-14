
class Factorial:

    def factorial_iterativo(self,n):
        """
        Calcula el factorial de un número de manera iterativa.
        Args:
          n: El número cuyo factorial se desea calcular.
        Returns:
          El factorial de n.
        """
        if n < 0:
            raise ValueError("El número debe ser mayor o igual a 0.")

        factorial = 1
        for i in range(1, n + 1):
            factorial *= i

        return factorial

    def factorial_recursivo(self,n):
        """
        Calcula el factorial de un número de manera recursiva.

        Args:
          n: El número cuyo factorial se desea calcular.

        Returns:
          El factorial de n.
        """
        if n < 0:
            raise ValueError("El número debe ser mayor o igual a 0.")

        if n == 0:
            return 1
        else:
            return n * self.factorial_recursivo(n - 1)