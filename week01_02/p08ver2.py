def numToArr(num):
    arr = []
    numAsStr = str(num)
    for x in numAsStr:
        arr.append(x)
    return arr

def zero_insert(n):
    numAsArr = numToArr(n)
    answers = []
    for x in range(0, len(numAsArr)):
        #print(numAsArr[x])
        if (((int(numAsArr[x]) + int(numAsArr[x - 1])) % 10) == 0):
            answers.append(0)
        answers.append(numAsArr[x])
    return answers

print(zero_insert(6446))