# Bomb ... 
'''
matrix = [[1,2,3],[4,5,6],[7,8,9]]

for row in range(0, 3):
    for col in range(0, 3):
        if (row, col) == (xBomb + 1, yBomb + 1):
            matrix[row][col] -= bombValue
'''

matrix = []
matrixLen = input("Matrix Len: ")
matrixLen = int(matrixLen)

for row in range(0, matrixLen - 2):
    for col in range(0, matrixLen - 2):
        print(matrix[row][col])

print(matrix)