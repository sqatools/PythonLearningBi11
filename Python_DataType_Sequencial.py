# String
"""
Properties:
1. String is immutable data type, once it is defined with can not change the values.
2. String following positive and negative indexing to traverse the data.
3. We can define string with single, double and triples quotes.

"""
str1 = 'Hello Good Morning'

str2 = "How are you"

str3 = '''We are learning Python
its easy to lear'''

str4 = """We are BI11 batch students and we
have started learning python"""

str5 = 'H'
str6 = "123456"
str7 = "My mobile number is 123456"
str8 = "Today is my 'BIRTHDAY' lets party"

# break the string in next line with \n
str9 = "We are BI11 batch students and we \n have started learning python"

# add spaces in the string with \t
str10 = "We are BI11 batch students and we \t\t\t have started learning python"

# convert a string into raw with r prefix before quotes

str11 = r"We are BI11 \n batch students and we \t\t\t have started \n learning python"

# print("str1 :", type(str1), str1)
# print("str2 :", type(str2), str2)
# print("str3 :", type(str3), str3)
# print("str4 :", type(str4), str4)
# print("str5 :", type(str5), str5)
# print("str6 :", type(str6), str6)
# print("str7 :", type(str7), str7)
# print("str8 :", type(str8), str8)
# print("str9 :", type(str9), str9)
# print("str10 :", type(str10), str10)
#print("str11 :", type(str11), str11)

# String Follows positive and negative indexing to traverse the data
#  0  1  2  3  4
# "H  e  l  l  o"
# -5 -4 -3 -2 -1

var1 = "Hello"

print(var1)
# positive index
print(var1[0])

# Negative index
print(var1[-5])

# print e from given string
print(var1[1], var1[-4])

var2 = "Good Morning"

#slicing
print(var2[2:])

# string method
print(dir(str))
# 'capitalize', 'casefold', 'center', 'count', 'encode',
# 'endswith', 'expandtabs', 'find', 'format', 'format_map',
# 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
# 'isdigit', 'isidentifier', 'islower', 'isnumeric',
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
# 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
# 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
# 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
# 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

###################################################################################
# list
"""
Properties :
1. List is mutable data type, once it is defined we can modify any numbers of time
2. List can contain any data object as member. int, float, string, list, tuple, dict, set
3. List Follows similar positive and negative indexing as like string.
"""
"""
list1 = ['h', 123, 45.7, 'Python']
list2 = [[3, 5], 'Hello', 4567 ]
list3 = [] # empty list

print("_"*20)
print(list1, type(list1))

# get data with positive index
print(list1[0])

# get data with negative index
print(list1[-1])

var11 = list1[-1]

print("var11 :", var11, type(var11))


print(var11[2])

######################### Get nested list from variable ###########

print("___"*50)
list11 = ['abc', [5, 7, 8], 345]

output = list11[1]
print(output)
# print 7 from nested list
print(output[1])

# multi dimention of the list
print(list11[1][1])
"""



"""
lista = [45, 78, 'Python',
         ['Programming', [2.5, 66, 'Language'],
          'Good', 'Morning'
          ]
         ]

# Print morning word from given list
print(lista[3][3])

# print language from nested list

print(lista[3][1][2])

"""


##########################################################

#Tuple

tup1 = (4, 6, 8, 'Hello', 'Morning', [4, 6, 8], (5, 6, 2, 3))

print(tup1, type(tup1))

# Get value with positive index
print(tup1[5])

print(tup1[5][1])

# Get value with negative index
print(tup1[-1])

print(tup1[-1][2])
"""
Properties:
1. Tuple is immutable data type, once it is defined with can not change the values.
2. Tuple following positive and negative indexing to traverse the data.
3. Tuple can contain any type of data as member int, float, string, list, tuple, etc.
"""















