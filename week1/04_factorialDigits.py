def factorial(n):
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result


def fact_digits(n):
    result = 0
    while(n > 0):
        lastNum = n % 10
        result += factorial(lastNum)
        n //= 10
    return result

if __name__ == "__main__":
    print(fact_digits(111))
    print(fact_digits(145))
    print(fact_digits(999))
