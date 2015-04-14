def sum_matrix(m):
    sumOfMatrix = 0
    for x in m:
        sumOfMatrix += sum(x)
    return sumOfMatrix


if __name__ == "__main__":
    print(sum_matrix([[1,2,3], [4,5,6], [7,8,9]]))
    print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))