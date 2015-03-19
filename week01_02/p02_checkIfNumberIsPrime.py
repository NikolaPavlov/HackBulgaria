def is_prime(a):
    isPrime = True
    if (a <= 1):
        isPrime = False

    for x in range(2, a - 1):
        if(a % x == 0):
            isPrime = False
    return isPrime


if __name__ == "__main__":
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(8))
    print(is_prime(11))
    print(is_prime(-10))
