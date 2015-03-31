def group(items):
    answers = []
    tempArr = []

    for x in range(0, len(items)):
        # Out of bounds stoper
        if x == len(items) - 1:
            break
        # Last elements case
        if x == len(items) - 2:
            tempArr.append(items[x])
            answers.append(tempArr)

        # Same elements, add them to tempArr
        if items[x] == items[x + 1]:
            tempArr.append(items[x + 1])

        # Deifferent element found, restart, null tempArr
        else:
            items[x] != items[x + 1]
            tempArr.append(items[x])
            answers.append(tempArr)
            tempArr = []

    return answers

if __name__ == "__main__":
    print(group([1, 1, 1, 2, 3, 1, 1, 1]))
    print(group([1, 2, 1, 2, 3, 3]))
