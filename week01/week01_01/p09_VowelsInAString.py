def count_vowels(input):
    input = input.lower()
    vowelsCount = 0
    for x in input:
        if (x == 'a'
            or x == 'e'
            or x == 'i'
            or x == 'o'
            or x == 'u'
            or x == 'y'):
            vowelsCount += 1
    return vowelsCount


if __name__ == "__main__":
    print(count_vowels("Python"))
    print(count_vowels("Theistareykjarbunga"))
    print(count_vowels("grrrrgh"))
    print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
    print(count_vowels("A nice day to code!"))
