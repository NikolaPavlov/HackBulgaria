def unique_words_count(arr):
    return len(set(arr))


if __name__ == "__main__":
    print(unique_words_count(["apple", "banana", "apple", "pie"]))
    print(unique_words_count(["python", "python", "python", "ruby"]))
    print(unique_words_count(["HELLO!"] * 10))