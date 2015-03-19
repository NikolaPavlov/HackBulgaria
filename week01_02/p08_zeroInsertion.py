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
        answers.append(numAsArr[x])

    print(answers)



zero_insert(11113343)
zero_insert(7557)