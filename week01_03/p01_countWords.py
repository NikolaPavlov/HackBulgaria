#TODO: Add sort in the dictonary
def count_words(arr):
    answers = {}
    for word in arr:
        if word not in answers:
            answers[word] = 1
        else:
            answers[word] += 1
    return answers


if __name__ == "__main__":
    print(count_words(["apple", "banana", "apple", "pie"]))
    print(count_words(["python", "python", "python", "ruby"]))