# from random import randint

# n = 6
# print([randint(1, 36) for x in range(n)])

# create multidimensional array
global_arr = []

print(global_arr)

for i in range(0, 11):
    for y in range(0, 11):
        global_arr.append("{}{}".format(i, y))

print(global_arr)

