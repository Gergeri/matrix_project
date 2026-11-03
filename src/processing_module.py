
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
