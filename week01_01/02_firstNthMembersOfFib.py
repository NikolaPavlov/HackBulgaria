# the return should be arr
def fibonacci(n):
    nums = []
    firstNum = 0
    lastNum = 1
    for x in range(0, n):
        tempNum = firstNum
        firstNum = lastNum
        lastNum = tempNum + lastNum
        nums.append(firstNum)
    return nums

if __name__ == "__main__":
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(10))
