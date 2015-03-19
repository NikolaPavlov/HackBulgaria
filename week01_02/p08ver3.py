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
        if (numAsArr[x] == numAsArr[x - 1]):
            answers.append(0)
        if (int(numAsArr[x]) + int(numAsArr[x - 1]) % 10) == 0:
            print('gg')
        answers.append(numAsArr[x - 1])
    print(answers)



zero_insert(11113343)
zero_insert(7557)