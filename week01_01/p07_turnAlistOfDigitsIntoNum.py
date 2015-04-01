def to_number(digits):
    numAsStr = ''
    for x in digits:
        numAsStr += str(x)
    return int(numAsStr)

if __name__ == "__main__":
    print(to_number([1, 2, 3]))
    print(to_number([9, 9, 9, 9, 9]))
    print(to_number([1, 2, 3, 0, 2, 3]))
