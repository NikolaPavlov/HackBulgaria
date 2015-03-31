from p04_NumberContainingASingleDigit import contains_digit


def contains_digits(number, digits):
    for digit in digits:
        if contains_digit(number, digit) == True:
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    print(contains_digits(402123, [0, 3, 4]))
    print(contains_digits(666, [6, 4]))
    print(contains_digits(123456789, [1, 2, 3, 0]))
    print(contains_digits(456, []))
