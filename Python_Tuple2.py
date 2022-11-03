tup1=(3,45,23,5,78,77,9,80,23,88,88,9,9,9,9,77,45,45)

outputt=[]
for i in tup1:
    if i%11==0:
        outputt.append(i**2)
    else:
        outputt.append(i**3)

print(outputt,  tuple(outputt))

import random
print(random.randint(0, 8))

list1 = [4, 6, 8, 2, 9, 1]

for i in range(5):
    rand_index= random.randint(0,  len(list1)-1)
    print(list1[rand_index], rand_index)

