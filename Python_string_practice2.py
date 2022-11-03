
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


# Write Python Program to get count of all the char
"""
str1= "We are learning Programming"

temp = ""

for char in str1:
    # char : W, e, " ", a
    # temp : "", "We a"
    if char not in temp:
        print(char,":", str1.count(char))
        temp = temp + char
    else:
        continue
"""

# Write Python Program to get count of all the char and print in dict form
# Output = {'W' : 1, "e": 3}
#dict1['key'] = 'value'
"""
str1= "We are learning Programming"

dict1 = {}

for char in str1:
    if char in dict1:
        continue
    else:
        dict1[char] = str1.count(char)

print("dict output:", dict1)
"""
"""
# Write Python Program to get count of all the char and print in dict form
# without using inbuilt method count
# Output = {'W' : 1, "e": 3}
# dict1['key'] = 'value'
str1= "We are learning Programming"
dict1 = {}
for char in str1:
    print(dict1, char)
    if char in dict1:
        dict1[char] += 1
    else:
        dict1[char] = 1
"""
###################################
# upper(), lower(), isupper(), islower()
"""

str1 = "GoodMorning"
# Convert all char to upper with upper() method
output =str1.upper()
print(output)

# Convert all char to lower case with lower() method
output2 =str1.lower()
print(output2)


# Check any given string is in upper case or not, same for lower case
str1 = "GoodMorning"
str2 = "GOOD"
output3 = str1.isupper()
print("output3 :", output3)  # False
output4 = str2.isupper()
print("output4 :", output4)  # True






# Check for lower case
str3 = "GoodMorning"
str4 = "good"

output5 = str3.islower()
output6 = str4.islower()
print("output5:", output5)
print("output6:", output6)
"""
# Write a python program to convert all the upper char to lower case and lower to upper()
str1 = "We arE LearnIng PYthon LaGuage"
output = ""
for char in str1:
    if char.isupper():
        temp = char.lower()
        output = output + temp
    elif char.islower():
        temp = char.upper()
        output = output + temp
    else:
        output = output + char
print(output)

############ Split method ###########
# split method : this method split the string with given delimeters and list of substrings or words
"""
str1 = "Today we are going to enjoy IND AuS Cricket Match"
str2 = "Its,very,positive,day,we,have,to,observe,it"
output = str1.split()  # Default parameter is space
print(output)

for word in output:
    print(word)

output2 = str2.split(",")
print(output2)
output3 = str2.split("e")
print(output3)
"""

#q Write a python program to print the pattern with given string
"""
str1 = "Python Programming is Easy To Learn"
#Output = "ppYTHONnn ppPROGRAMMINgg iiss eeASyy ttoo llEARnn"
result = ""
word_list = str1.split(" ")
print(word_list)
for word in word_list:
    #print(word)
    first_char = word[0]
    last_char = word[-1]
    bw_first_last = word[1:-1]
    result_word = f"{(first_char*2).lower()}{bw_first_last.upper()}{(last_char*2).lower()}"
    #print(word, ":", result_word)
    result = result + result_word + " "

print("result :", result)
"""
# Index method : Get index of any character in the given string

str1 = "Python"
output = str1.index("y")
print("index of y:", output)
print(str1[output])

output2 = str1.index("o")
print("index of o:", output2)
print(str1[output2])

str2 = "Programming"

for i in range(len(str2)):
    print(str2[i],":", i)


# Replace : Replace any character to another one in the given string.
# replace is with are in the given string
"""
str1 = "Python Programming is Easy To Learn"

output = str1.replace("is", "are")
print(output)

output2 = str1.replace("m", "n")
print(output2)

output3 = str1.replace(" ", "")
print(output3)
"""
"""
# Write a python program to replace vowels with special character $.
#str1 = "Python Programming is Easy To Learn"
#output = "Pyth$n Pr$gr$mm$ng $s E$sy T$ L$$rn"
str1 = "Python Programming is Easy To Learn"
vowels = "aeiou"
result = ""
word_list = str1.split()
for word in word_list:
    for char in word:
        if char.lower() in vowels:
            word = word.replace(char, "$")
        else:
            continue
    result = result + word + " "
print("result :", result)
"""
"""
#### strip method : remove all trailing spaces from the given string.

str1 = "    Very Good Morning   "
print(str1)
output = str1.strip()
print(output)

#lstrip : remove space from left side of the string
output2 = str1.lstrip()
print(output2)

#rstrip : remove space from right side of the string
output3 = str1.rstrip()
print(output3)


test_str = "https://www.google.co.in"
output = test_str.split(".")
print(output)
output2 = output[0].split("//")
print(output2)
w_var = output2[1]
print(w_var)

w_result = test_str.split(".")[0].split("//")[1]
print("w_result:", w_result)

# Replace Scenario
str1 = "Hello my name is yogesh and i am working in facebook my salary 2lac"
output = str1.replace('yogesh', 'tushar').replace('facebook', 'google').replace('2lac', '3lac')
print(output)
"""

#################################
# find method : check any word/sub-string is available in the given string
# if available then it will return index of that substring, else it will return -1
str1 = "Hello my name is yogesh and i am working in facebook my salary 2lac"

output = str1.find('Yogesh')
print(output) # -1
output2 = str1.find('yogesh')
print(output2) # 17

# swapcase : convert upper to lower and lower to upper
str1 = "Hello my NamE s Yogesh and i am wOrking in Facebook my Salary 2lac"
output = str1.swapcase()
print(output)

# class work
# Write a python to covert all odd length word to capital and even length word to small case

# title method
str1 = "Hello my NamE s Yogesh and i am working in Facebook my Salary 2lac"

output = str1.title()
print(output)




































