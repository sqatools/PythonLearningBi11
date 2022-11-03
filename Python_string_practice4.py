str1 = "progra#mming123"

# isalnum : this method return true if string only contains char and digits, if we have any space
# or special character then it will return False
output = str1.isalnum()
print(output)

# Program1 : get all the alpha numeric words in the given string.
# str1 = "Python123 lan34 567 progra#mming123"
# output = "Python123 lan34 567"

#---------------------------
stra = "abc"
strb = "abc1243"
strc = "1243"

# isdigit () : This method return true if the string contain only numbers
"""
output1 = stra.isdigit()
print(output1) # False

output2 = strb.isdigit()
print(output2)  # False

output3 = strc.isdigit()
print(output3) # True
"""
# Program2 : get all the numbers in the given string.
# str1 = "Python 123 lan 34 567 progra#mming 333"
# output = "123 34 567 333"

# output = output + word + " " # add space in word.

strp = "1.45"

output1 = strp.isnumeric()
print(output1)

output2 = strp.isdigit()
print(output2)


# Program3 : program get all the mobile numbers in the given string.
# str1 = "Python 123 9834224555 lan 34 567 progra#mming 333  9834224335 java 9994224555"
# output = "9834224555 9834224335 9994224555"

# join method : though this method we can join all the string with any delimeter

strx = "Programming"

output = "_".join(strx)
print(output)

# programs4 : python program to join each word with special delimeters
str1 = "How are you, very"
#output = "H_o_w a-r-e y#o#u#, v*e*r*y"

str1 = "How are you, very"
#output2 = "H__o__w a--r--e y##o##u##, v**e**r**y"

print("_"*50)
word_list = str1.split()
print(word_list)
spec_var = "_-#*"
output = ""

for i in range(len(word_list)):
    #print(word_list[i], spec_var[i])
    new_word = spec_var[i].join(word_list[i])
    #print(i , word_list[i], spec_var[i], new_word)
    output = output + new_word + " "

print(output)

# Program5 : Program to get all the email id from given string
str1 = "we have test2@test.com some employee whose emails id are sagar@gmail.com," \
       "anand@hotmail.com test1@gmail.com  admin@admin.com"

output = " test2@test.com sagar@gmail.com anand@hotmail.com test1@gmail.com  admin@admin.com"