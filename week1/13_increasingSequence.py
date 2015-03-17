def is_increasing(seq):
    for x in range(1, len(seq)):
        if (seq[x] > seq[x - 1]):
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    print(is_increasing([1, 2, 3, 4, 5]))
    print(is_increasing([1]))
    print(is_increasing([5, 6, -10]))
    print(is_increasing([1, 1, 1, 1]))
