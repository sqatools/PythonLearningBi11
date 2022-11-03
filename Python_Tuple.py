# Tuple
#         0  1   2         3          4
tuple1 = (5, 7, 'morning', [5, 7, 8], 2.5)
#        -5  -4  -3        -2         -1

print(tuple1, type(tuple1))
# positive index
output = tuple1[3]
print(output)
print(output[1])

# Negative index
output2 = tuple1[-1]
print(output2)

# Apply slicing on tuple
tup1 = (4, 7, 2, 8, 1)

print(tup1[1: 5])  # (7, 2, 8, 1)
print(tup1[: 3])  # (4, 7, 2)
print(tup1[2:])   # (2, 8, 1)
print(tup1[0::2])  # (4, 2, 1)
print(tup1[::-1])  # (1, 8, 2, 7, 4)

# Tuple Methods.
print(dir(tuple))
# print(dir(int))
# print(dir(str))
# print(dir(list))
#
"""
print(list.__doc__)
print("_"*30)
print(int.__doc__)
print("_"*30)
print(tuple.__doc__)

num1 = 20
num2 = 30
print(num1.__add__(num2))
print([4, 6, 7].__add__([5, 7, 2]))
"""

#'count', 'index'

tup1 = (5, 7, 2, 8, 5, 12, 2, 5)
# count

output = tup1.count(5)
print(output)

# Class program : get count of each element in the tuple and add into dictionary
#tup1 = (5, 7, 2, 8, 5, 12, 2, 5)
#output = {5:3, 7:1, 2:2, 8:1, 12:1}


# Get index of specific element
tup1 = (5, 7, 2, 8, 5, 12, 2, 5)

output1 = tup1.index(12)
print(output1)

"""
# Program : write a python program to get square of all the number which are divide 11
# and cube of remaining, make sure output should in tuple.
tup1 = (5, 77, 2, 8, 11, 12, 22, 5)

# Program : Write a python program with print following output.

tup2 = ("Hello", "Good", "Morning", "How", "Are", "You")
# Remove all the duplicate char from each string
output1 = ("Helo", "God", "Mornig", "How", "Are", "You")
# First and last chars will key and remaining chars will the value in the output dict.
output2 = {"Ho": "ello", "Gd": "oo", "Mg": "orning", "Hw": "o", "Ae": "r", "Yu": "o"}
"""

# Combine all the element in the tuple
"""
tup1 = (5, 7, 8)
tup2 =  (2, 3, 4)

tup3 = tup1 + tup2
print(tup3)
"""

# Repeat  tuple and list n number of time
tup4 = (6, 8, 2)
list1 = [5, 7, 8]
print(tup4*3)

print(list1*2)

#####################
tup5 = (5, 7, 3)
list1 = [5, 2, 8]
#tup5[1] = 10 it does not support

list1[1] = 10

print(list1)