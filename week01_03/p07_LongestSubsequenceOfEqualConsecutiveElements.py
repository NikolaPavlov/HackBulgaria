def max_consecutive(items):
    maxCount = 0
    localCount = 1
    for x in range(0, len(items)):
        if x > len(items) - 2:
            break
        if items[x] == items[x + 1]:
            localCount += 1
        else:
            if localCount > maxCount:
                maxCount = localCount
                localCount = 1

    return maxCount


if __name__ == "__main__":
    print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
    print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
