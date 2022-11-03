import time

# Nested loop
# i : address
# j : package

"""
for i in range(1, 6):
    for j in range(1, 4):
        print("address :", i, "Package:", j)

    print("__"*20)
"""

# Write a program to get prime number
# The number which can divide itself or 1 is known as prime number.
# 2, 3, 5, 7, 11, 13, 17


"""
num = 100000
Prime = True

t1 = time.time()
for i in range(2, num):
    #print(i)
    if num%i == 0:
        Prime = False

if Prime:
    print("This number is prime number :", num)
else:
    print("This is not prime number :", num)
t2 = time.time()
total_time_taken = t2-t1
print(total_time_taken)

"""

# Optimize solution2
"""

num = 100000
Prime = True
t1 = time.time()
for i in range(2, num//2):
    print(i)
    if num%i == 0:
        Prime = False

if Prime:
    print("This number is prime number :", num)
else:
    print("This is not prime number :", num)
t2 = time.time()

total_time = t2-t1
print("Total time:", total_time)

"""

# Optimize solution3

"""
num = 100000
Prime = True
t1 = time.time()
if num%2 == 0:
    Prime = False
else:
    for i in range(3, num//2, 2):
        print(i)
        if num%i == 0:
            Prime = False

if Prime:
    print("This number is prime number :", num)
else:
    print("This is not prime number :", num)
t2 = time.time()

total_time = t2-t1
print("Total time:", total_time)

"""

# Write python program to get list of prime numbers between 1 to 100
"""
for n in range(2, 100): # n = 2, 3, 4, 5
    prime= True
    for i in range(2, n):
        if n%i == 0:
            prime = False
        else:
            continue

    if prime:
        print(n)
"""



# continue and break statement
"""
for i in range(10):
    if i == 3 or i == 4:
        continue
    print(i)

print("_"*20)
for i in range(10):
    if i == 5:
        break
    print(i)


num = 41

for i in range(2, num//2):
    if num%i==0:
        prime = False
        break
    else:
        prime = True


if prime:
    print("this is prime number :",num)
else:
    print("this is not prime number :", num)
"""

# Write a python program to print below Pyramid

"""
*
* *
* * *
* * * *
* * * * *
"""
"""
for i in range(6):
    for j in range(i):
        print("*", end=" ")
    print()


print("\n")
"""
"""
* * * * *
* * * *
* * *
* *
* 
"""
"""
for i in range(6, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
"""
"""
1  2  3  4  5  6
7  8  9 10 11
12 13 14 15
15 17 18
19 20
21
"""
"""
temp = 1
for i in range(6, 0, -1):
    for j in range(i):
        print(temp, end="   ")
        temp = temp + 1
    print()
"""
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
#import  pdb; pdb.set_trace()


""
"""
var1 = 3
var2 = 5

for i1 in range(5):
    for j1 in range(9):
        #v1 : 3, 2, 1, 0
        #v2 : 5, 6, 7, 8
        #j1 : 0, 1, 2, 3, 4, 5, 6, 7, 8,
        #     _  _  _  _  *  _  _  _  _
        #j1 : 0, 1, 2, 3, 4, 5, 6, 7, 8
        #     _  _  _  *  *  *  _  _  _
        #j1:  0, 1, 2, 3, 4, 5, 6, 7, 8
        #j1:  _  _  *  *  *  *  *  _  _
        #j1:  0, 1, 2, 3, 4, 5, 6, 7, 8
        #     _  *  *  *  *  *  *  *, _
        if j1 > var1 and j1 < var2:

            print("*", end=" ")
        else:
            print("_", end=" ")
    print("\n")

    var1 = var1 - 1
    var2 = var2 + 1
    
"""
# While Loop condition

"""
while condition:
    code
"""

"""
num = 0

while num <= 10:
    print(num)
    num = num + 1
"""
# print table any give number
"""
table = 3

num = 1

while num <= 10:
    print(num, "*", table, ":", num*table)
    num = num + 1
"""

# Infinite loop with while
"""
num = 1
while True:
    print(num)
    num = num+1
"""

"""
# continue running calculator
while True:
    print("Please enter your input:\n"
          "1. addition\n"
          "2. subtract\n"
          "3. multiply\n"
          "4. divide")

    user_input = int(input("Please enter your choice :"))

    var1 = int(input("Please enter value for var1:"))
    var2 = int(input("Please enter value for var2:"))

    if user_input == 1:
        print("Addition :", var1+var2)
    elif user_input == 2:
        print("subtraction :", var1 - var2)
    elif user_input == 3:
        print("Multiply :", var1 * var2)
    elif user_input == 4:
        print("Divide :", var1 // var2)
    print("\n\n\n")
"""


# Reverse any given number

num1 = 43546789
#output = 321

#3*10 + 2 = 32
#32*10 + 1 = 321
reverse = 0
while num1 > 0:
     temp = num1%10
     reverse = reverse*10 + temp
     num1 = num1//10

print("reverse :", reverse)



#########################


word = input("Input a word to reverse: ")
output = ""
for char in range(len(word)- 1, -1, -1):

  print(word[char], ":", char)
  output = output + word[char]
print("\n")

print("output :", output)