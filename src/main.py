# Программа для перестановки строк матрицы с минимальным и максимальным элементами

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


def find_min_max(matrix):
    min_value = matrix[0][0]
    max_value = matrix[0][0]
    min_row = 0
    max_row = 0

    for i in range(len(matrix)):
        for value in matrix[i]:
            if value < min_value:
                min_value = value
                min_row = i

            if value > max_value:
                max_value = value
                max_row = i

    return min_row, max_row


def swap_rows(matrix, max_row, min_row):
    matrix[max_row], matrix[min_row] = matrix[min_row], matrix[max_row]


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def main():
    while True:
        matrix = input_matrix()

        print("\nИсходная матрица:")
        print_matrix(matrix)

        min_row, max_row = find_min_max(matrix)
        swap_rows(matrix, max_row, min_row)

        print("\nМатрица после перестановки строк:")
        print_matrix(matrix)

        repeat = input("\nПродолжить? (да/нет): ").strip().lower()
        if repeat != "да":
            break


if __name__ == "__main__":
    main()