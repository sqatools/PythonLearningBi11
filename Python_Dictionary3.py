# Dictionary Method

print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
# 'popitem', 'setdefault', 'update', 'values']

dict1 = {'a': 345, 'b' : 234, 'c' : 123}
# Get all keys from the dict using keys methods.
output = dict1.keys()
print(output)
# Get all values from the dict
output2 = dict1.values()

# program : reverse the values in the dict and repeat keys
#          2 times from given dict.
dict1 = {45 : 'Python', 'Tech': [5, 7, 2, 8],
         (5,2, 7) : 4562, 3.78: [5, 7, [5, 8, 9], 1]}
Output = {90 : 'nphtyP', 'TechTech': [8, 2, 7, 5],
          (5, 2, 7, 5, 2, 7) :  2654, 7.5 : [1, [9, 8, 5], 7, 5]}

num = 'char'
if type(num) == type(1):
    print('Int type')
if isinstance(num, int):
    print("True")
else:
    print("False")


# check any data is available in dict
"""
dict1 = {'a': 345, 'b' : 234, 'c' : 123}

output2 = 'd' in dict1
print(output2)
"""
# remove data from the dictionary.
dict1 = {'a': 345, 'b' : 234, 'c' : 123, 'd': 56, 'e': 12}
output2 = dict1.pop('c')
print(output2, dict1)


# Program :  write a python to move data from one dict to another dict.
# -> if key is int then divide by 3 and consider remainder as key
      #-> if remainder is 0 then set key as 1.
"""
# -> if key as already available in the output dict then add values in list.

dict1 = {5: 'Hello', 7: 123, 8: (5, 2, 7), 11: 'Python', 10: [5, 8, 2]}
#output = {2: ['Hello', (5, 2, 7),'Python'], '1' : [123, [5, 8, 2]]}
#dict1 = {}
"""
"""
# pop items
output3 = dict1.popitem()
print("output3 :", output3)
"""
#  Clear all the data from the dict'

dict1 = {5: 'Hello', 7: 123, 8: (5, 2, 7), 11: 'Python', 10: [5, 8, 2]}
dict1.clear()
print("dict1:", dict1)


# Update data from one dict to another

dict1 = {'a': 567, 'b' : 234, 'c': 534}
dict2 = {'p': 123, 'q': 567, 'r' : 121}
dict1.update(dict2)
print("dict1 :", dict1)
print("dict2 :", dict2)

# Program : write a python program to get common keys from give dicts
# and add their values

dict1 = {'a': 567, 'b' : 234, 'c': 534}
dict2 = {'p': 123, 'q': 567, 'r' : 121, 'a': 453, 'b': 345}
output = {'a' : 1020, 'b': 579}

# Items:
dict33 = {'p': 123, 'q': 567, 'r' : 121, 'a': 453, 'b': 345}
print(dict33.items())
for key, value in dict33.items():
    print("key:", key, "value:", value)

list1 = ['p', 'q', 'r']
list2 = [4, 6, 7]
output3 = zip(list1, list2)
print(output3)
list1 = []
for data in output3:
    #print(data)
    list1.append(data)
print(dict(list1))


lista = ['p', 'q', 'r']
listb = [4, 6, 7]

outputa = zip(lista, listb)
print(outputa)

outputb = [data for data in outputa]
print(outputb)
print(dict(outputb))