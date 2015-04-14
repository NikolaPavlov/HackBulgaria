def is_credit_card_valid(number):
    newNum = '0'
    sumOfDigits = 0

    # The len of number is even number, invalid card
    if len(str(number)) % 10 == 0:
        return False

    # Create the new number
    while number != 0:
        lastDigit = number % 10
        newNum += str(lastDigit)
        number //= 10
        nextToLastDigit = number % 10
        newNum += str(nextToLastDigit * 2)
        number //= 10

    # Sum all digits of the new num
    newNum = int(newNum)
    while newNum != 0:
        lastDigit = newNum % 10
        sumOfDigits += lastDigit
        newNum //= 10

    return sumOfDigits % 10 == 0

if __name__ == "__main__":
    print(is_credit_card_valid(79927398713))
    print(is_credit_card_valid(79927398715))
