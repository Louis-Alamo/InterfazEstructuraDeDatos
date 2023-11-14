
class Fibonaci:

    def fibonacci_iterativo(self,n):
        """
        Genera la serie Fibonacci de manera iterativa.

        Args:
          n: El número de términos de la serie que se desean generar.

        Returns:
          La serie Fibonacci de n términos.
        """

        if n == 0 or n == 1:
            return [n]
        else:
            fibonacci = [0, 1]
            for i in range(2, n + 1):
                fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
            return fibonacci

    def fibonacci_recursivo(self,n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            fib_sequence = self.fibonacci_recursivo(n - 1)
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
            return fib_sequence