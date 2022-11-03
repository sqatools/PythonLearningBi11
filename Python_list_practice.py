list1 = [3, 5, 'a', 'b', 'c']

print(list1[0])
print(list1[-1])
print(list1, type(list1))

print(dir(list))

# 'append', 'clear', 'copy',
# 'count', 'extend', 'index',
# 'insert', 'pop', 'remove',
# 'reverse', 'sort'

# Slicing
"""
#         0  1  2  3  4    5     6
list11 = [5, 7, 2, 8, 'a', 'b', 'Hello']
#        -7  -6 -5 -4 -3   -2     -1
# rule2 : list1[first_index: last index]

output1 = list11[1:5]
print("Output1:", output1)  # [7, 2, 8, 'a']

output1 = list11[2:6]
print("Output1:", output1) # [2, 8, 'a', 'b']



# rule2 : list1[: last_index] # default first index will be zero
list22 = [5, 7, 2, 8, 'a', 'b', 'Hello']
print(list22[:3])   # [5, 7, 2]

#rule3 : list1[first_index:] # default last index will end value of the list
list22 = [5, 7, 2, 8, 'a', 'b', 'Hello']
print(list22[2:])   # [2, 8, 'a', 'b', 'Hello']


# rule4 : list1[first_index::jump of index value]
list33 = [5, 7, 2, 8, 'a', 'b', 'Hello']

output33 = list33[0::1]  # start from zero with one index jump
print(output33)  # [5, 7, 2, 8, 'a', 'b', 'Hello']

output44 = list33[0::2]  # start from zero with two index jump
print(output44)  # [5, 2, 'a', 'Hello']

output55 = list33[2::3]  # start from 2 second with 3 index jump
print(output55)  # [5, 2, 'a', 'Hello']

# with negative index
lista = [5, 7, 2, 8, 'a', 'b', 'Hello']

output6 = lista[-1::-1]     # start from -1 index with -1 index jump
print("output6:", output6)  # ['Hello', 'b', 'a', 8, 2, 7, 5]

output6 = lista[-2::-2]  # start from -2 index with -2 index jump
print("output6:", output6)  # ['b', 8, 7]
"""

######## List methods ######

listb = [5, 8, 3, 2.5, 'a']

# append method : this method add element to the list at the end index or add in the last
"""
num = 40
listb.append(num)

print("listb", listb)

listb.append([4, 6, 7]) # add child list to list
listb.append(('a', 'b', 'c')) # add tuple to the list
listb.append('Morning') # add string to the list
listb.append({"name": "Akshay", "Age": 23}) # add dict to the list
listb.append({'p', 'q', 'r'})

print("listb", listb)
# [5, 8, 3, 2.5, 'a', 40, [4, 6, 7], ('a', 'b', 'c'), 'Morning', {'name': 'Akshay', 'Age': 23}, {'p', 'q', 'r'}]
output = listb[-1]
print(output)
print(listb[6][2])  #7
print(listb[9]["name"]) # Akshay
listb[6].append(8)  # add data to child list
print("listb :", listb)

listb[9]['email'] = 'Akshay@gmail.com'   # add data to member dict
print("listb :", listb)
"""

"""
# program : add data from one list to another list
listp = [5, 8, 2, 9, 3]
listq = []

for var in listp:
    listq.append(var)

print("listq :", listq)
"""

# Program : Add even data and odd data in separate list from given list
list1 = [5, 7, 2, 8, 3, 44, 11]
odd_list = [5, 7, 3, 11]
even_list = [2, 8, 44]

# Program : program to add square of even and cube of odd number in seprate
# list between from 1 to 20
# even : square
# odd : cube


###### extend method : this method add one list to another list
"""
listx = [5, 7, 2, 8, 3]
listy = [4, 6, 1]

listx.extend(listy)
print("listx :", listx)

# combine two list data with plus operator :
list11 = [5, 7, 2, 8, 3, 11, 22]
list22 = [4, 6, 1, 66]
output = ['a', 'b', 'c']

#output = list11 + list22
#print("output :", output)

output = output + list11 + list22
print(output)
"""

# insert method : add data to the specific index of the list
"""
listr = ['Python', 'Java', 'shell', 'a', 'b']
listr.insert(1, 'Javascript')
print(listr)

listr.insert(-2, 'Program')
print(listr)

# Program : insert all the number which are divide by 3 at zero index and number
# divide by 7 add in the -1 index
# list1 = [15, 77, 63, 23, 21, 35, 42, 49, 45]
# output = [45, 42, 21, 63, 15, 77, 35, 49]
list1 = [15, 77, 63, 23, 21, 35, 42, 49, 45]
output = []
for var in list1:
    if var%3 == 0:
        output.insert(0,  var)
    elif var%7 == 0:
        output.insert(len(output), var)
    else:
        continue

    print(output)
"""

####################### Remove Data from the list ############

# remove method : we can remove specific element from the list using remove method.
"""
list11 = [5, 7, 8, 2, 9]
list11. remove(8)
print("list11: ", list11)


list22 = [5, 7, 8, 2, 9, 5]
# if there is duplicate element in the list then it will delete first occurance
list22.remove(5)
print("list22: ", list22)
"""

# pop method : pop method can remove any element from specific index, return the same element.
"""
list33 = [5, 7, 8, 2, 9, 5, 88]

# pop method take default index as -1
output = list33.pop()
print("output :", output)
print("list33 :", list33)

# remove data from specific index e.g 4
output1 = list33.pop(4)
print("output1 :", output1) # 9
print("list33 :", list33)   # [5, 7, 8, 2, 5]
"""

"""
# Program : to remove all the data from one list and move to another list.
list1 = [5, 3, 6, 7, 16, 8]
#output1 = [5, 3, 6, 7, 16, 8]
#list1 = []
output1 = []

for i in range(len(list1)):
    var = list1.pop(-1)
    #output1.append(var)
    output1.insert(0, var)

print("output1:", output1)
print("list1", list1)

#HW: Program : program to move data from one list to another with their data type
list1 = ['a', 3, 5, 6, 6.7, 'Hello', 'b', 'c', 2.5]
str_list = []
int_list = []
float_list = []

if type(2.3) == type(1.1):
    print(True)
else:
    print(False)
"""
"""
# Delete entire list
list22 = [5, 7, 8]
print("list22 :", list22)

del list22
print("list22 :", list22)
"""



# Clear Method

list1 = [5, 3, 7, 2, 8]

list1.clear()

print(list1, " :list1")





# Sorting of the list data
"""
lista = [5, 7, 2, 1, 6, 8]

#sort method : this method sort the list in accending order and change the list inplace.
lista.sort()  # Sorting of the list in accending order
print(lista)  # [1, 2, 5, 6, 7, 8]

output = lista.sort(reverse=True)  # Sorting of the list in decending order
print(lista, output)  # [8, 7, 6, 5, 2, 1]

# sorted method
listb = [4, 1, 8, 2, 9, 10]
outputb = sorted(listb)
outputb1 = sorted(listb, reverse=True)

print("listb :", listb)
print("outputb :", outputb)
print("outputb1 :", outputb1)
"""

# Reverse the list data
listq = [5, 3, 7, 2, 8]
listq.reverse()
print("listq:", listq)

listr = [5, 3, 7, 2, 8, 33, 12]
outputr = reversed(listr)
for var in outputr:
    print(var, end=" ")
print("outputr:", outputr)
print("listr:", listr)

# HW : reverse the list with loop, while loop and slicing