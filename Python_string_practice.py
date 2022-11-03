str1 = "Hello Good Morning"

print(str1, type(str1))

# positive index , start with 0
# negative index, starts with -1 from reverse order

print(str1[0])

print(str1[-1])

# String formatting



#Output = "Hello my name is Yogesh and my age is 25 and i am living in Pune"

"""
str1 = "Python"
str2 = "Programming"

output = str1 +" "+ str2
print(output)
"""

# name = "Yogesh"
# age = 25
# address = "Pune"
"""
name = input("Please enter your name:")
age = input("Please enter your age:")
address = input("Please enter your address:")

# Format1 : concatination with + plus operator
output1 = "Hello my name is "+name+" and my age is "+str(age)+" and i am living in "+ address
print(output1)

# Formate2 : string combination with format method

output2 = "Hello my name is {} and my age is {} and i am living in {}".format(name,  age, address)
print(output2)

# Format3 : f string format

output3 = f"Hello my name is {name} and my age is {age} and i am living in {address}"
print(output3)
"""

################# String Slicing ########
str1 = "Programming"
# 0  1  2  3  4  5  6  7  8  9  10
#"P  r  o  g  r  a  m  m  i  n  g"
#-11-10-9 -8 -7 -6 -5 -4  -3 -2 -1

# Rule1: str1[initial index: end index]
# In this rule , substring will contain initial index and return sub string till end_index-1

output = str1[1: 5]
print(output)  # rogr

output2 = str1[-4: -1]
print("Output2 :", output2)  # min

# Rule : str[initial_index:]
# In this rule it will return entire substring from intial_index to end_index which is by default last
# char

output3 = str1[3:]
print(output3)  #gramming

output4 = str1[10:]
print(output4)  #g

output5 = str1[-6:]
print("output5 :", output5)

# Rule3 : str[:last_index]
# In this rule, default initial index is 0 and return substring from zero index to last_index-1

output6 = str1[:5]
print("output6 :", output6) # Progr

output7 = str1[:-4]
print("output7 :", output7) # Program

# Rule4 : str[initial_index::index difference]
# in this rule use has to define initial index and different of index between each index value

output8 = str1[0::1]
print("output8 :", output8)  # Programming

output9 = str1[0::2]
print("output9 :", output9)  # Pormig

output10 = str1[3::2]
print("output10 :", output10)  # gamn

output11 = str1[-1::-1]
print("output11 :", output11)  #gnimmargorP

# Rule5 : str[::difference_index]
# In this rule default positive index will zero and return substring with given difference of index
# In this rule default negative index will be -1

output12 = str1[::1]
print("output12 :",output12)

output12 = str1[::2]
print("output12 :",output12)

# In case of negative index , default initial index will be -1
output13 = str1[::-1]
print("output13 :",output13)

#Rule6 : str[initial_index::]

output14 = str1[2::]
print("output14 :",output14)  #ogramming

output15 = str1[-4::]
print("output15 :",output15)  #ming


################################################
# String Methods
print(dir(str))
"""
'capitalize', 'casefold', 
'center', 'count', 'encode', 'endswith', 
'expandtabs', 'find', 'format', 'format_map', 
'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
'isdigit', 'isidentifier', 'islower', 'isnumeric', 
'isprintable', 'isspace', 'istitle', 'isupper', 'join', 
'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 
'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
 'startswith', 'strip', 'swapcase', 
 'title', 'translate', 'upper', 'zfill'
"""
"""
Useful Method 
-> count
-> 'find', 'format',
-> 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal'
-> 'isdigit', 'islower', 'isnumeric'
-> 'isspace', 'istitle', 'isupper', 'join'
-> 'ljust', 'lower', 'lstrip'
-> 'replace', 'rfind', 'rindex'
-> 'rsplit', 'rstrip', 'split', 'splitlines'
-> 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
"""

# Count Method : This method calculate total occurance of any character in given string.

str1= "We are learning Programming"
# Get toal occurance of g

output = str1.count('g')
print(output)
















