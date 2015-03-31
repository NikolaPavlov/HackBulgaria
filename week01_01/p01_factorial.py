def factorial(n):
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    print(factorial(0))
    print(factorial(1))
    print(factorial(5))
