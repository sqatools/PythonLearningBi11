# Reverse the string.
str1 =  "Good Morning"

#1 : slicing to reverse the string

output = str1[::-1]
print(output)

# program to find any given string is palimdrop or not
"""
input_str = input("Please enter the input:")

rever_str = input_str[::-1]
if input_str  == rever_str:
    print("String is palindrome")
else:
    print("String is not palindrome")
"""
# reverse the sting with for loop
"""
str1 = "dood"
rever_Str = ""

for i in range(-1, -len(str1)-1, -1):
    print(str1[i])
    rever_Str = rever_Str + str1[i]

print(rever_Str)

if str1 == rever_Str:
    print("this is palindrome")
else:
    print("this is not palindrome")
"""

# reverse the string with for while loop
"""
str1 = "Good Morning"

str_len = len(str1)
temp = -1
rever_str = ""
print(str_len)

while temp >= -str_len:
    print(str1[temp],temp)
    rever_str = rever_str + str1[temp]
    temp = temp - 1

print("Reverse string:", rever_str)

if str1 == rever_str:
    print("this is palindrome")
else:
    print("this is not palindrome")
"""

# Program to find out all the palindrome words in given string.

str1 = "Ptyhon sis bestseb programming lal"
#output = "sis bestset lal"

"""
1 : defind output= "" as variable
2 : get word_list using list word_list = str1.split()
3 : apply loop on word list to get each word "for word in word_list"
4 : check if reverse of the word and actual word is equal if word == word[::-1]
5 : if both values are equal, then add in output var output = output + word + " "
6 : if both are not equal then continue
7  : then print output out of the loop
"""
"""
output = ""
word_list = str1.split()
for word in word_list:
    if word == word[::-1]:
        output = output + word + " "
        print(output)
    else:
        continue
print("Output : ", output)
"""

# Write python program to get longest word in the string

#str11 = "Python sis bestseb programming lal"
"""
1. set variable long_word = "" long_len = 0
2. get word list with split method word_list = str1.split()
3. apply loop on word_list "for word in word_list".
4. Get word length word_len = len(word)
5. check if word_len is greater than long_len 
6. if yes then long_word = word and long_len = word_len
7. if not then continue
8. print(long_word, long_len)
"""
str11 = "sdfsadfasdfasdfasfaaa Python sis bestseb programming lal  sdfsadfasdfasdfasfdas"
# step1
long_word = ""
long_len = 0
#step2
word_list = str11.split()
#step3
for word in word_list:
    #step4
    word_len = len(word)
    if word_len >= long_len: # 0 > 6, 3>6, 7> 6, 11> 7, 3> 11
        long_len = word_len # 0, 6, 6, 7, 11, 11
        long_word = word # "", python, python, bestseb, programming
    else:
        continue

print(long_word, long_len)

#1 Program to find out smallest word in the given string
str11 = "sdfsadfasdfasdfasfaaa Python sis bestseb programming lal  sdfsadfasdfasdfasfdas"
output = "sis"

#2 Program to replace all the character with # whose index divide by 3 or 7
str11 = "sdfsadfasdfasdfasfaaa Python sis bestseb programming lal  sdfsadfasdfasdfasfdas"

#3 Program to count all the vowels in each word in the string.
str1 = "Python sis bestseb programming"
output = {"Python": 1, "sis": 1, "bestseb": 2, "programming": 3}


######################

# 2 Program to replace all the character with # whose index divide by 3 or 7
# str11 = "sdfsadfasdfasdfasfaaa Python sis bestseb programming lal  sdfsadfasdfasdfasfdas"

"""
1. set a variable with output = ""
2. Get string length with len method str_len = len(str1)
3. apply loop on string length. "for i in range(str_len)"
4. check given index value is divide by 3 or 7 : if i%3 == 0 or i%7 == 0
5. if yes then replace that char with # : output = output + "#"
6. if not then add char in output "output = output + str1[i]"
7. print(output)
"""

str11 = "Good"
#output11 = "G##d"
output11 = ""
vowels = "aieou"

for char in str11:
    #print(char)
    if char in vowels:
        output11 = output11 + "#"
    else:
        output11 = output11 + char

print("output 11:", output11)

print("_"*25)
output22 = ""
for i in range(len(str11)):
    #print(str11[i])
    if str11[i] in vowels:
        output22 = output22 + "#"
    else:
        output22 = output22 + str11[i]

print("output22:", output22)



#3 Program to count all the vowels in each word in the string.
#str1 = "Python sis bestseb programming"
#output = {"Python": 1, "sis": 1, "bestseb": 2, "programming": 3}

"""
1. set variable ,   = {},  vowels = "aieou"
2. get word list with split method word_list = str1.split()
3. apply loop on word_list and get each word "for word in word_list"
4. set a variable with count = 0
5. apply loop on word to get each char "for char in word"
6. check that given char is in vowels "if char in vowels"
7. If yes then we will increase count value by 1
8. if not then continue in else.
9. Now we have set word and its vowels count out of char loop output_dict[word] = count
10. print output_dict
"""

