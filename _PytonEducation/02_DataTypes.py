# 1. Tuple (tuples are immutable)
data = tuple(["Nikola", "Pavlov", 6, 6])
print(data)
# unpacking tuple
first_name, second_name, grade1, grade2 = data
print(first_name)
print(second_name)
print(grade1)
print(grade2)

# 2. Sets (array with unique elements)
setA = set([1,2,1,3,1,2])
print(setA)

# 3. Dictonaries
myBio = {'name': 'Nikola', 'age': 30, 'hobby': 'hacking'}

# check if key exsist
if 'name' in myBio:
    print(myBio['name'])
# return tuple key: value pear
print(myBio.items())
myBio['location'] = 'Sofia'
print(myBio)
del myBio['location']
print(myBio)
