matrix = [[1,2,3], [4,5,6], [7,8,9]]

print ([matrix[len(matrix)-1-i][i] for i in range(len(matrix)-1,-1,-1)])