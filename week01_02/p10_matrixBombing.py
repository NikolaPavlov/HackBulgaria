def matrix_bombing_plan(m):
    dictionary = {}

    for row in range(0,len(m)):
        for col in range(0,len(m)):
            bombed = m
            coordinates = row,col
            bomb = bombed[row][col]
            bombed = [bombed[row][col] - bomb for row in range(len(m)) for col in range(len(m)) if bombed[row][col] >= bomb]
            dictionary[coordinates] = sum(bombed) + bomb

    return dictionary