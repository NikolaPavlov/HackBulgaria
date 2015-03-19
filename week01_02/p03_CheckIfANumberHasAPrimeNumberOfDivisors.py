from p02_checkIfNumberIsPrime import is_prime


def primeNumberOfDivisors(n):
    answers = []
    for x in range(1, n):
        if (n % x == 0):
            answers.append(x)
    answers.append(n)
    return is_prime(len(answers))


if __name__ == "__main__":
    print(primeNumberOfDivisors(7))
    print(primeNumberOfDivisors(8))
    print(primeNumberOfDivisors(9))

