import keyword

print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as',
# 'assert', 'async', 'await', 'break',
# 'class', 'continue', 'def', 'del',
# 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import',
# 'in', 'is', 'lambda', 'nonlocal', 'not',
# 'or', 'pass', 'raise', 'return', 'try',
# 'while', 'with', 'yield']

a = 20
b = 30

"""
if condition:
   code
"""

"""
if b > a:
    print("b is greater than a")
"""
"""
conditional operator

> : greater than
< : less than
>= : greater than equal to
<= : less than equal to
== : equal to operator
!= : not equal to (not)

AND OR
"""

"""
num2 = 31

if num2%2 == 0:
    print("this is even number")
"""
"""
if condition:
    code
else:
    code
"""

"""
num3 = 51

if num3%2 == 0:
    print("This number is even number:", num3)
else:
    print("This number is odd number:", num3)
"""

"""
AND
condition1 AND condition2

TRUE and TRUE : TRUE
FALSE and TRUE : FALSE
TRUE and FALSE : FALSE
FALSE and FALSE : FALSE
"""

a = 9

#  TRUE and TRUE : a = 12
#  TRUE and FALSE : a = 22
#  FALSE and TRUE : a = 9

"""
if a > 10 and a < 20:
    print("a is greater than 10 and less than 20")
else:
    print("condition is not satisfied")
    a = 24

print(a)
"""


"""
OR

TRUE or TRUE : TRUE
FALSE or TRUE : TRUE
FALSE or FALSE : FALSE
TRUE or FALSE : TRUE
"""

a = 10

# FALSE or TRUE : TRUE  : a = 9
# TRUE or TRUE : TRUE : a = 12
# TRUE or FALSE : TRUE : a = 25
# FALSE or TRUE : TRUE  : a = 10
# FALSE or FALSE : FALSE : a = 9
# TRUE or FALSE : FALSE : a = 10

if a >= 10 or a > 20:
    print("Condition is satisfied.")
else:
    print("condition is not satisfied.")


# Program : find out given number is divible by 7 and 3

#user_input = int(input("Please enter your input:"))

"""
if user_input%3 == 0 and user_input%7 == 0:
    print("the number can divide by 3 and 7 :", user_input)
else:
    print("the number can not divide by 3 and 7 :", user_input)

"""

"""
if user_input%3 == 0 or user_input%7 == 0:
    print("the number can divide by 3 or 7 :", user_input)
else:
    print("the number can not divide by 3 or 7 :", user_input)
"""



# Program2 : write program to check any number can divide by 5
# program3 : write program to check if input number is square of 7.
# Program4 : Write a program to check given number is divisible by 13 and 5


user_input = int(input("Please enter your input:"))

if user_input%13 == 0 or user_input%5 == 0:
    print("The Number is divisible by 13 and 5 :", user_input)
else:
    print(" The Number is not divisible by 13 and 5 : ", user_input)