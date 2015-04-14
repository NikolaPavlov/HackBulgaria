# Check if number is prime
def is_prime(a):
    isPrime = True
    if (a <= 1):
        isPrime = False

    for x in range(2, a - 1):
        if(a % x == 0):
            isPrime = False
    return isPrime


# Return all prime nums in range(2, n)
def findPrimesInRange(n):
    primeNumbers = []

    for num in range(2, n):
        if is_prime(num):
            primeNumbers.append(num)
    return primeNumbers


# Create the result
def goldbach(n):
    answers = []
    tempAnswers = []

    primeNumbers = findPrimesInRange(n)

    for i in range(0, len(primeNumbers)):
        for j in range(i, len(primeNumbers)):
            if primeNumbers[i] + primeNumbers[j] == n:
                tempAnswers.append(primeNumbers[i])
                tempAnswers.append(primeNumbers[j])
                answers.append(tempAnswers)
                tempAnswers = []
    return answers


# nice formating the output (tuples)
def formatTheResult(n):
    results = goldbach(n)
    output = []

    for arr in results:
        output.append((arr[0], arr[1]))

    return output


if __name__ == "__main__":
    print(formatTheResult(4))
    print(formatTheResult(6))
    print(formatTheResult(8))
    print(formatTheResult(10))
    print(formatTheResult(100))

