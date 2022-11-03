#### Integer #######

# int -> float :  its possible
"""
num1 = 30

print(num1, type(num1))
output = float(num1)

print(output, type(output))

"""

# int -> string
"""
num1 = 3045676

print(num1, type(num1))

str1 = str(num1)
print(str1, type(str1))

# get string value with index
print(str1[3])
"""

# int -> list : conversion is not possible
"""
num1 = 567889

print(num1, type(num1))
list1 = list(num1)
print(list1)
"""
# TypeError: 'int' object is not iterable

# int -> tuple : conversion is not possible
# TypeError: 'int' object is not iterable

# int -> dict : conversion is not possible
"""
num1 = 34567
print(num1, type(num1))

dict1 = dict(num1)
print(dict1, type(dict1))

# TypeError: 'int' object is not iterable
"""

# int -> set # conversion is not possible
"""
num1 = 5678
print(num1, type(num1))
set1 = set(num1)
print(set1, type(set1))

TypeError: 'int' object is not iterable
"""

################## Float ##############

# float -> int
"""
num1 = 45.66
print(num1, type(num1))

output = int(num1)
print(output,  type(output))
"""

# float -> string
"""
num1 = 45.66
print(num1, type(num1))

str1 = str(num1)
print(str1, type(str1))

print(str1[2])  # .
print(str1[3])  # 6

"""

# Float -> list : conversion is not possible
"""
num1 = 45.77
output = list(num1)
print(output)
#TypeError: 'float' object is not iterable
"""

# float -> tuple : conversion is not possible
"""
num1 = 45.77
output = tuple(num1)
print(output)
# TypeError: 'float' object is not iterable
"""

# Float -> dict :  conversion is not possible
"""
num1 = 45.77
output = dict(num1)
print(output)
# TypeError: 'float' object is not iterable
"""

# Float -> set : conversion is not possible

"""
num1 = 45.77
output = set(num1)
print(output)
# TypeError: 'float' object is not iterable
"""

######################## String ##################

# string -> int # If string contains numbers only then we can convert into int, otherwise
#conversion is possible
"""
str1 = "3456"

num1 = int(str1)
print(num1, type(num1))
"""
"""
str2 = "H234"

num2 = int(str2)
print(num2)
# ValueError: invalid literal for int() with base 10: 'H234'
"""

###### String -> float
"""
str1 = "45.90"
num1 = float(str1)

print(num1, type(num1))
"""
"""
str2 = "Hello123"

num2 = float(str2)
print(num2)
# ValueError: could not convert string to float: 'Hello123'
"""

#### String -> list
"""
str1 = "Hello"

output = list(str1)
print(output, type(output))

print(output[2])   #l
"""
##### String -> tuple

str1 = "Hello"

output = tuple(str1)
print(output, type(output))

print(output[-1])   # o

### String -> dict : any normal string conversion to dictionary is not possible
"""
# error:
#ValueError: dictionary update sequence element #0 has length 1; 2 is required

str1 = "Good Morning"

dict1 = dict(str1)
print(dict1, type(dict1))
"""
"""
We can convert a string into dict which is dictionary format with the help of json module
import json

str2 = '{"a": 234, "b": 567, "c": 222}'

json_data = json.loads(str2)

print(json_data['a'])

print(json_data, type(json_data))

json_data['d'] = 4567
print(json_data)
"""

# String -> set # set conversion only store unique characters, duplicate characters will be removed.
"""
str1 = "Programming"
output = set(str1)
print(output, type(output))
"""
############## List ###############

# list -> int : Conversion is not possible
"""
list1 = [5, 7, 8, 2]

output = int(list1)
print(output)
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
"""


#### List -> Float : conversion is not possible

"""
list1 = [5, 7, 8, 2]

output = float(list1)
print(output)
"""
# TypeError: float() argument must be a string or a real number, not 'list'


#### list -> string

"""
list1 = [5, 7, 3, 8]

output = str(list1)
print(output, type(output))

print(output[0])
print(output[1])
"""

##### list -> tuple

"""
list1 = [4, 7, 2, 8]

output = tuple(list1)
print(output, type(output))

print(output[1])

"""

###### list -> dict : list to dict conversion is not possible
"""
list1 =[5, 7, 8, 2, 8]
output = dict(list1)
print(output)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence
"""


#### list -> set # list to set conversion remove all the duplicate data from the list

list1 = [5, 7, 2, 8, 1, 6, 2, 1]

output = set(list1)
print(output,  type(output))

################# Tuple ##############

# tuple -> int : conversion is not possible
# tuple -> float : conversion is not possible
# tuple -> string
"""
tup1 = (5, 7, 2, 8)
output = str(tup1)
print(output, type(output))

print(output[0])
print(output[2])
print(output[4])
"""

# Tuple -> list
"""
tup1 = (5, 7, 2, 8)
list1 = list(tup1)

print(list1, type(list1))
print(list1[-1])  # 8
"""

# Tuple -> dict : Conversion is not possible
# Tuple -> set # with tuple to set conversion all duplicate values will be removed.

tuple1 = (5, 7, 2, 7, 'a', 'b', 'a', 7)

output = set(tuple1)
print(output, type(output))


###### dictionary ###########

# dict -> int : not possible
# dict -> float : not possible
# dict -> string
"""
dict1 = {'name': 'rahul', 'age': 45}
output = str(dict1)
print(output, type(output))

print(output[0])
print(output[1])
print(output[2])
"""

# dict -> list :  If we will convert dict to list, then it will print all the keys only

dict1 = {'a': 123, 'b': 456}

output = list(dict1)
print(output)

# dict -> tuple : If we will convert dict to tuple then it will print only tuple of keys in the
# dictionary
dict2 = {'a': 123, 'b': 456}

output2 = tuple(dict2)
print(output2)

# dict -> set :   not possible




########  Set ##########

# set -> int : not possible
# set -> float : not possible
# set -> string
"""
set1 = {5, 6, 8, 'a', 'b'}

str1 = str(set1)
print(str1, type(str1))

print(str1[0], str1[1])

"""

# set -> list
"""
set1 = {5, 6, 8, 'a', 'b'}

list1 = list(set1)
print(list1, type(list1))

print(list1[0], list1[-1])
"""

# set -> Tuple
"""
set1 = {5, 6, 8, 'a', 'b'}

tup1 = tuple(set1)

print(tup1, type(tup1))
print(tup1[0])
"""

# Set -> dict : not possible
