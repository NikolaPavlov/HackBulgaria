def magic_square(matrix):
    sums = []

    # sum all rows
    for row in matrix:
        sums.append(sum(row))

    # sum all cols
    for i in range(0, len(matrix)):
        sums.append(sum(row[i] for row in matrix))

    # sum of diagonal
    sums.append(sum(matrix[i][i] for i in range(len(matrix))))

    # sum of the other diagonal
    sum_of_other_diagonal = 0
    for j in range(len(matrix) - 1, -1 , -1):
        sum_of_other_diagonal += matrix[i][j]
        i += 1
    sums.append(sum_of_other_diagonal)

    print(sums)


if __name__ == "__main__":
    magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])