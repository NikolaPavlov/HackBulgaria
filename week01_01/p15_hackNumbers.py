# wtf I can't import for files started with digits!    _/_ this sh17
def reverseTxt(obj):
    objAsStr = str(obj)
    answer = ''
    for x in reversed(range(0, len(objAsStr))):
        answer += objAsStr[x]
    return answer


def palindromeCheckBinaryNum(num):
    numAsBinary = bin(num)
    newNumAsBinary = ''
    for x in range(2, len(numAsBinary)):
        newNumAsBinary += numAsBinary[x]
#    print(newNumAsBinary)
    return newNumAsBinary == reverseTxt(newNumAsBinary)


def oddNumberOfOnesCheck(num):
    numInBinary = bin(num)
    numOfOnes = 0
    for digit in numInBinary:
        if (digit == '1'):
            numOfOnes += 1
    if (numOfOnes % 2 == 1):
        return True
    else:
        return False


def next_hack(num):
    while(True):
        num += 1
        if (palindromeCheckBinaryNum(num)):
            if (oddNumberOfOnesCheck(num)):
                return num
                break

if __name__ == "__main__":
    print(next_hack(0))
    print(next_hack(10))
    print(next_hack(8031))
