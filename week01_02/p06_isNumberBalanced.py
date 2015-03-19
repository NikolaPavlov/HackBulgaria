def is_number_balanced(n):
    numAsStr = str(n)
    halfLen = len(str(n)) // 2
    leftSum = 0
    rightSum = 0

    for x in range(0, halfLen):
        leftSum += int(numAsStr[x])

    reversedNumAsStr = numAsStr[::-1]
    for x in range(0, halfLen):
        rightSum += int(reversedNumAsStr[x])

    if (leftSum == rightSum):
        return True
    return False


if __name__ == "__main__":
    print(is_number_balanced(9))
    print(is_number_balanced(11))
    print(is_number_balanced(13))
    print(is_number_balanced(121))
    print(is_number_balanced(4518))
    print(is_number_balanced(28471))
    print(is_number_balanced(1238033))
