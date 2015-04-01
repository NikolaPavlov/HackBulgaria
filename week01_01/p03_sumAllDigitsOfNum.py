def sum_of_digits(n):
    # negative to positive numbers
    if (n < 0):
        n *= -1

    result = 0
    while (n > 0):
        lastDigit = n % 10
        result += lastDigit
        n //= 10
    return result

if __name__ == "__main__":
    print(sum_of_digits(1325132435356))
    print(sum_of_digits(123))
    print(sum_of_digits(6))
    print(sum_of_digits(-10))
