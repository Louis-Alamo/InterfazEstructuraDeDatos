class ShellSort():

    @staticmethod
    def shell_sort(arr):
        n = len(arr)
        gap = n // 2
        comparaciones = 0
        pasadas = 0
        movimientos = 0

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                pasadas += 1

                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                    comparaciones += 1
                    movimientos += 1

                arr[j] = temp
                movimientos += 1

            gap //= 2

        return comparaciones, pasadas, movimientos