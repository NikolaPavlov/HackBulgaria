# TODO: mine func work with any characters, should work only with a and b
def is_an_bn(word):
    if len(word) % 2 != 0:
        return False

    # Check left side
    for i in range(0, int(len(word) / 2)):
        # Out of bounds stop
        if i == len(word) / 2 - 1:
            break

        if word[i] != word[i + 1]:
            return False

    # Check right side, copy paste like a boss :)
    for i in range(int(len(word) / 2), len(word)):
        # Out of bounds stop
        if i == len(word) - 1:
            break

        if word[i] != word[i + 1]:
            return False

    return True


if __name__ == "__main__":
    print(is_an_bn(""))
    print(is_an_bn("rado"))
    print(is_an_bn("aaabb"))
    print(is_an_bn("aaabbb"))
    print(is_an_bn("aabbaabb"))
    print(is_an_bn("bbbaaa"))
    print(is_an_bn("aaaaabbbbb"))
