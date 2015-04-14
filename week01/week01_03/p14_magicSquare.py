def magic_square(matrix):
    all_sums = []

    # sum all rows
    for row in matrix:
        all_sums.append(sum(row))

    # sum all cols
    for i in range(0, len(matrix)):
        sum_of_one_col = 0
        for j in range(0, len(matrix)):
            sum_of_one_col += matrix[j][i]
        all_sums.append(sum_of_one_col)

    # sum of first diagonal
    sum_of_diagonal = 0
    for i in range(0, len(matrix)):
        sum_of_diagonal += matrix[i][i]

    all_sums.append(sum_of_diagonal)

    # sum of second diagonal
    sum_of_diagonal = 0
    j = len(matrix) - 1
    for i in range(0, len(matrix)):
        sum_of_diagonal += matrix[i][j]
        j -= 1
    all_sums.append(sum_of_diagonal)

    # check if all numbers in all_sums are equal
    if len(set(all_sums)) == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
