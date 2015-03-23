# There is no easy import in python
# fuck this shit I will be gamer 
def is_prime(a):
    isPrime = True
    if a <= 2:
        return False

    for x in range(2, a):
        if(a % x == 0):
            isPrime = False
    return isPrime


def prime_nums_into_list(n):
    primeNums = []
    for x in range(0, n):
        if is_prime(x):
            primeNums.append(x)
    return primeNums

list = prime_nums_into_list(n)

def main(arr):
    for num in arr:
        for strep in 





print(prime_nums_into_list(55))
