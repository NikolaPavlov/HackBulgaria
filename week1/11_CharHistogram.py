# TODO: Fix appearence in return value
def char_histogram(string):
    dictonary = {}
    for x in string:
        if (x in dictonary):
            dictonary[x] += 1
        else:
            dictonary[x] = 1
    return dictonary

if __name__ == "__main__":
    print(char_histogram("Python!"))
    print(char_histogram("AAAAaaa!!!"))
