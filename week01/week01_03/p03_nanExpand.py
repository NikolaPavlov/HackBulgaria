def nan_expand(times):
    result = ""
    for x in range(0, times):
        result += "Not a "
    result += "NaN"
    return result

if __name__ == "__main__":
    print(nan_expand(1))
    print(nan_expand(2))
    print(nan_expand(3))
    print(nan_expand(4))
