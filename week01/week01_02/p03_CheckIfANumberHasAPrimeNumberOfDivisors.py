from p02_checkIfNumberIsPrime import is_prime


def prime_number_of_divisiors(n):
    answers = []
    for x in range(1, n):
        if (n % x == 0):
            answers.append(x)
    answers.append(n)
    return is_prime(len(answers))


if __name__ == "__main__":
    print(prime_number_of_divisiors(7))
    print(prime_number_of_divisiors(8))
    print(prime_number_of_divisiors(9))

