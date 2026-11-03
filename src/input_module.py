
def input_matrix():
    while True:
        try:
            n = int(input("Введите количество строк: "))
            m = int(input("Введите количество столбцов: "))

            if n <= 0 or m <= 0:
                print("Размеры матрицы должны быть положительными.")
                continue

            matrix = []

            for i in range(n):
                while True:
                    try:
                        row = list(map(float, input(
                            f"Введите {m} элементов строки {i + 1}: "
                        ).split()))

                        if len(row) != m:
                            print(f"Необходимо ввести ровно {m} элементов.")
                            continue

                        matrix.append(row)
                        break

                    except ValueError:
                        print("Ошибка. Введите числовые значения.")

            return matrix

        except ValueError:
            print("Ошибка. Размеры матрицы должны быть целыми числами.")
