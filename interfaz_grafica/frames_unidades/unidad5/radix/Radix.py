class RadixSort:
    def print_queues(self, queues):
        for i, q in enumerate(queues):
            if q:
                print(f"[{i}] --->  {', '.join(map(str, q))}")

    def radixsort(self, arr):
        NUMELTS = len(arr)
        exp = 1
        pasadas = 0
        comparaciones = 0
        movimientos = 0

        while True:
            max_num = max(arr)
            if max_num // exp == 0:
                break

            pasadas += 1
            count = [0] * 10
            output = [0] * NUMELTS
            queues = [[] for _ in range(10)]

            for i in range(NUMELTS):
                index = int((arr[i] // exp) % 10)
                count[index] += 1
                queues[index].append(arr[i])

            print("\nColas basadas en el dígito más significativo")
            self.print_queues(queues)

            for i in range(1, 10):
                count[i] += count[i - 1]

            i = NUMELTS - 1
            while i >= 0:
                comparaciones += 1
                index = int((arr[i] // exp) % 10)
                output[count[index] - 1] = arr[i]
                count[index] -= 1
                i -= 1

            for i in range(NUMELTS):
                movimientos += 1
                arr[i] = output[i]

            exp *= 10

        return  pasadas, movimientos,comparaciones