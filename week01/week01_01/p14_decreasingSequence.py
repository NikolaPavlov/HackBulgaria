def is_decreasing(seq):
    for x in range(1, len(seq)):
        if (seq[x] < seq[x - 1]):
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    print(is_decreasing([5, 4, 3, 2, 1]))
    print(is_decreasing([1, 2, 3]))
    print(is_decreasing([100, 50, 20]))
    print(is_decreasing([1, 1, 1, 1]))