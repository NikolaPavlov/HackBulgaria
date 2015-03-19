def zero_insert(n):
    numbers = list(map(int, str(n)))
    result = []
    result2 = []

    if (len(numbers) == 1):
        return numbers

    # same digits one after another check
    for i in range(0, len(numbers) - 1):
        result.append(numbers[i])
        if (numbers[i] == numbers[i + 1]):
            result.append(0)
        #lame check fot index out of boundes
        #if we hit next to last element
        #add last element manualy
        if (i == len(numbers) - 2):
            result.append(numbers[len(numbers) - 1])

    if len(result) > 0:
        numbers = result

    # digits one after another % 10 == 0 check
    for i in range(0, len(numbers) - 1):
        result2.append(numbers[i])
        if ((numbers[i] + numbers[i + 1]) % 10) == 0:
            result2.append(0)

        #lame check fot index out of boundes
        #if we hit next to last element
        #add last element manualy
        if (i == len(numbers) - 2):
            result2.append(numbers[len(numbers) - 1])

    return result2


if __name__ == "__main__":
    print(zero_insert(116457))
    print(zero_insert(55555555))
    print(zero_insert(6446))
