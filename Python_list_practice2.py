# Deep Copy Shallow Copy

# Shallow copy
"""
list1 = [4, 6, 8, 2, 7, 12]
list2 = list1
list3 = list2
list4 = list3

list2.append(30)
list4.append(33)

print("list1:", list1)
print("list2:", list2)
print("list4:", list4)
"""

############################
"""
# Deep Copy
lista = [5, 6, 2, 7, 12, 66]
listb = lista.copy()
listb.append(50)
lista.append(60)

print("listb :", listb)
print("lista :", lista)
"""
################################
"""
listx = [5, 7, 3, 8, 2]
listy = [1, 55, 14, 23]
listx.append(30)

listz = listx + listy
listr = listz
listr.append(100)

print("listx :", listx)
print("listy :", listy)
print("listz :", listz)
print("listr :", listr)
"""
#########################
list11 = [5, 7, 2, 8, 3]

list22 = list11.copy()
list33 = list11

for i in range(len(list22)):
    list22.append(list22[i]**2)

print("list22 :", list22)
print("list11 :", list11)


for i in range(len(list33)):
    list33.append(list33[i]**2)

print("list33 :", list33)
print("list11 :", list11)


######################################
print("_"*40)
# Get sum of all the list numbers in the list
list11 = [5, 7, 8, 2, 8, 3, 5] # with loop class work

sum_of_data = sum(list11)
print("Sum of all data:",  sum_of_data)

max_of_data = max(list11)  # with loop find max value in the list class work
print("Max of all data:",  max_of_data)

min_of_data = min(list11)  # with loop find min value in the list class work
print("Min of all data:",  min_of_data)

##################################################
print("_"*40)
# program : get square of all the number from the list
list11 = [4, 2, 6, 1, 7, 11, 13, 14]
output = []
for var in list11:
    output.append(var**2)
print(output)

output2 = [var**2 for var in list11]
print(output2)

# If condition with list comprehension
output3 = [var for var in list11 if var%2 == 0]
print("output3 :", output3)

# If else condition with list comprehension
output4 = [(var, "even") if var%2==0 else (var, "odd") for var in list11]
print("output4:", output4)

# Nested loop with list comprehension
output5 = [(f"x:{x}", f"y:{y}") for x in range(5) for y in range(3)]
print("output5:", output5)

output6 = [(f"x:{x}", f"y:{y}") for x in range(5) for y in range(x)]
print("output6:", output6)

for x in range(5):
    for y in range(x):
        print("*", end=" ")
    print()








