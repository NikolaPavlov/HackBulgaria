def contains_digits(number, digits):
    numberAsStr = str(number)
    for digit in digits:
        if str(digit) not in numberAsStr:
            return False
    return True


if __name__ == "__main__":
    print(contains_digits(402123, [0, 3, 4]))
    print(contains_digits(666, [6, 4]))
    print(contains_digits(123456789, [1, 2, 3, 0]))
    print(contains_digits(456, []))