def count_consonants(input):
    inputAsLowerCase = input.lower()
    consonants = set('b''c''d''f''g''h''j''k''l''m''n''p''q''r''s''t''v''w''x''z')
    countConsonants = 0
    for x in inputAsLowerCase:
        if (x in consonants):
            countConsonants += 1
    return countConsonants

if __name__ == "__main__":
    print(count_consonants("Python"))
    print(count_consonants("Theistareykjarbunga"))
    print(count_consonants("grrrrgh"))
    print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
    print(count_consonants("A nice day to code!"))
