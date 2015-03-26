def reverseTxt(obj):
    objAsStr = str(obj)
    answer = ''
    for x in reversed(range(0, len(objAsStr))):
        answer += objAsStr[x]
    return answer


def palindrome(obj):
    return str(obj) == reverseTxt(obj)

if __name__ == "__main__":
    print(palindrome(121))
    print(palindrome("kapak"))
    print(palindrome("baba"))
