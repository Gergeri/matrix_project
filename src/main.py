
from src.input_module import input_matrix
from src.processing_module import find_min_max, swap_rows
from src.output_module import print_matrix


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
