def fib_number(n):
    nums = []
    firstNum = 0
    lastNum = 1
    for x in range(0, n):
        tempNum = firstNum
        firstNum = lastNum
        lastNum = tempNum + lastNum
        nums.append(firstNum)
    # add all nums into string, then convert to int
    numAsStr = ''
    for x in nums:
        numAsStr += str(x)
    return int(numAsStr)

if __name__ == "__main__":
    print(fib_number(3))
    print(fib_number(10))

