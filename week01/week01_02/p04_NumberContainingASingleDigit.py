def contains_digit(number, digit):
    while(number > 0):
        lastDigit = number % 10
        if (lastDigit == digit):
            return True
            break
        number //= 10
    return False


if __name__ == "__main__":
    print(contains_digit(123, 4))
    print(contains_digit(42, 2))
    print(contains_digit(1000, 0))
    print(contains_digit(12346789, 5))