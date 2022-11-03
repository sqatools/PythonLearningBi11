func = lambda x, y: x+y
print(func(5, 6))

# Map # Filter # Reduce
def factor(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact

list1 = [4, 5, 7, 8, 9]

output = list(map(lambda x: x**2, list1))
print(output)

output1 = list(map(factor, list1))
print(output1)

# Filter
list1 = [4, 5, 7, 8, 9]

output3 = list(filter(lambda x: x%2 == 0, list1))
print(output3)

# Reduce
from functools import  reduce

output4 = reduce(lambda x,y : x+y , list1)
print(output4)

