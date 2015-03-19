def sum_of_divisors(n):
    answers = []
    for x in range(1, n):
        if (n % x == 0):
            answers.append(x)
    answers.append(n)
    return sum(answers)


if __name__ == "__main__":
    print(sum_of_divisors(8))
    print(sum_of_divisors(7))
    print(sum_of_divisors(1))
    print(sum_of_divisors(1000))