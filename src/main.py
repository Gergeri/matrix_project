
try:
    from src.input_module import input_matrix
    from src.processing_module import find_min_max, swap_rows
    from src.output_module import print_matrix
except ImportError as error:
    raise SystemExit(f"Ошибка загрузки модуля: {error}")


def main():
    while True:
        try:
            matrix = input_matrix()

            if not matrix or not matrix[0]:
                raise ValueError("Матрица не должна быть пустой.")

            print("\nИсходная матрица:")
            print_matrix(matrix)

            min_row, max_row = find_min_max(matrix)
            swap_rows(matrix, max_row, min_row)

            print("\nМатрица после перестановки строк:")
            print_matrix(matrix)

        except (ValueError, TypeError, IndexError) as error:
            print(f"Ошибка обработки данных: {error}")
            break

        repeat = input("\nПродолжить? (да/нет): ").strip().lower()
        if repeat != "да":
            break


if __name__ == "__main__":
    main()
