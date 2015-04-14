def to_digits(n):
    result = []
    while (n > 0):
        result.append(n % 10)
        n //= 10
    result.reverse()
    return result

if __name__ == "__main__":
    print(to_digits(123))
    print(to_digits(99999))
    print(to_digits(123023))
