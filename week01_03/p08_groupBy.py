# shit happens
def groupby(func, seq):
    return{result: [elem for elem in seq if func(elem) == result]
    for result in set([func(elem) for elem in seq])}


if __name__ == "__main__":
    print(groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))
    print(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
    print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))