from p05_palindrome import palindrome, reverseTxt

def p_score(n):
    if palindrome(n):
        return 1

    s = n + int(str(n)[::-1])
    return 1 + p_score(s)


if __name__ == "__main__":
    print(p_score(121))
    print(p_score(48))
    print(p_score(198))