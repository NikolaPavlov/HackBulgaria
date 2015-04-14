def is_prime(a):
    if (a <= 1):
        return False

    for x in range(2, a - 1):
        if(a % x == 0):
            return False
    return True


def prime_factorization(n):
    prime_divisors = []
    factorization = tuple()

    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            prime_divisors.append(i)

    for divisor in prime_divisors:
        count = 0
        while n % divisor == 0:
            count += 1
            n /= divisor

        factorization += ((divisor, count), )
    return factorization

print(prime_factorization(10))
print(prime_factorization(14))
print(prime_factorization(356))
print(prime_factorization(1000))
