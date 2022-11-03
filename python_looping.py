# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# range
"""
for var in range(10):
    print(var)
"""

# range(initial value,  end value, increment value)
# default initial value 0
# default incremental value 1


for var in range(10):
    print(var)

print("_" * 10)
for var in range(0, 10, 2):
    print(var)

print("_" * 10)
for var in range(2, 50, 3):
    print(var)

# print number from 2 to 20 with default increment 1
print("_" * 10)
for var in range(2, 20):
    print(var)

# print numbers from 20 to 1
print("_" * 10)
for var in range(20, 0, -1):
    print(var)

# Program : print number from 1 to 20 and ignore number between 10 to 15.
print("_" * 10)
for i in range(1, 20):
    if i >= 10 and i <= 15:
        print(-i)
        continue
    print(i)

# Program : apply loop list
print("_" * 20)
list1 = ['Tech Focus', 1234, 'a', 56, 4.5]

for var in list1:
    print(var)

# Get all the even number from the list
print("_" * 20)
list2 = [4, 6, 23, 11, 5, 66, 77]

for var in list2:
    if var % 2 == 0:
        print(var)

# Apply loop on string
str1 = "Hello Good"
print("_" * 20)
for var in str1:
    print(var)

# print output in single line
print("_" * 20)
for var in str1:
    print(var, end=" ")

# Apply loop on tuple values

tup1 = (4, 6, 23, 11, 44, 21)
print("_" * 20)
print("_" * 20)
"""
for var in tup1:
    print(var)
    
for var in tup1:
    print(var)
"""
#
# Nested Loop condition
for i in range(5):
    for var in tup1:
        print(var, var)

tup1 = (4, 6, 23, 11, 44, 21)
# Program : print all the value from tuple which belongs between 10 to 30
print("_" * 20)
for var in tup1:
    if var > 10 and var < 30:
        print(var)

# Apply loop with dictionary
print("_" * 20)
dict1 = {'name': 'Yogesh', 'age': 40, 'address': 'Pune'}

for val in dict1:
    print(val)

print("_" * 20)
for key, val in dict1.items():
    print(key, ":", val)

# apply look on sets

set1 = {5, 6, 7, 2, 8, 5}

for val in set1:
    print(val)

print("_" * 20)
for i in range(20, 30):
    if i == 22 or i == 28:
        continue
    print(i)
