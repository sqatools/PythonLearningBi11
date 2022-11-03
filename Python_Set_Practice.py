set1 = {5, 7, 2, 'a', 'Hello', (5, 7, 8), 7, 5}
print(set1, type(set1))

# we can not add list as set member
"""
set2 = {5, 7, 2, 'a', 'Hello', (5, 7, 8), 7, 5, [5, 8, 2]}
# TypeError: unhashable type: 'list'
print(set2, type(set2))
"""

# We can not list and dict as member of set.
"""
set3 = {5, 7, 2, 'a', 'Hello', (5, 7, 8), 7, 5, {'a': 123}}
print(set3)  # TypeError: unhashable type: 'dict'
"""
# method of set datatype
print(dir(set))

# 'add', 'clear', 'copy', 'difference', 'difference_update',
# 'discard', 'intersection', 'intersection_update',
# 'isdisjoint', 'issubset', 'issuperset', 'pop',
# 'remove', 'symmetric_difference', 'symmetric_difference_update',
# 'union', 'update'

# Add data to the set
set11 = {1}
set11.add(5)

print(set11)

set22 = {5, 7, 8}
set33 = {6, 1, 9}


"""
output = set22 + set33
# # TypeError: unsupported operand type(s) for +: 'set' and 'set'
print(output)
"""
#'clear', 'copy', 'difference', 'difference_update',
# clear :
set33 = {7, 2, 8, 'a'}

set33.clear()
print("output:", set33)

# copy data from one to another
# Deep copy
"""
setx = {7, 2, 8, 'a'}
seta = setx.copy()
print(seta)
seta.add(50)

print("seta :", seta)
print("setx :", setx)

# shallow copy
setb = setx
setb.add(100)
print("setb :", setb)
print("setx :", setx)
"""

# Remove data from sets
setw = {4, 6, 2, 8, 1}
setw.remove(2)
print("setw :", setw)  # {1, 4, 6, 8}

# Pop data from the set, remove and return the element
sety = {'a', 4, 6, 22, 'c', 8, 11, 'b'}
elem = sety.pop()
print("elem:", elem)
print("sety:", sety)

"""
sety1 = {'a', 4, 6, 22, 'c', 8, 11, 'b'}
setx1 = set()

for i in range(len(sety1)):
    #print("elem :", elem)
    data = sety1.pop()
    setx1.add(data)


print("setx :", setx1)
print("sety :", sety1)
"""

##########################################

# union of two sets
"""
seta = {5, 7, 2, 8, 'a', 'b'}
setb = {10, 20, 4, 8, 5}

output = seta.union(setb)

print("seta :", seta)
print("setb :", setb)
print("output :", output)
"""
"""
# difference of two set
seta = {5, 7, 2, 8, 'a', 'b'}
setb = {10, 20, 4, 8, 5}

output1 = seta.difference(setb)  # {'a', 2, 'b', 7}
print("output1 :", output1)

output1 = setb.difference(seta)  # {'a', 2, 'b', 7}
print("output1 :", output1)

# get symmatric values
# symmetric_difference : get combination all the non symmentric values from both sets.
seta = {5, 7, 2, 8, 'a', 'b'}
setb = {10, 20, 4, 8, 5}
output3 = seta.symmetric_difference(setb)  # {2, 4, 7, 20, 'a', 'b', 10}
print(output3)

# Get common element from both the set
seta = {5, 7, 2, 8, 'a', 'b'}
setb = {10, 20, 4, 8, 5}

output4 = seta.intersection(setb)
print(output4)  # {8, 5}

# Update data from one to another

setg = {5, 2, 7, 1, 8}
setp = {11, 67, 23, 45}

setg.update(setp)
print("setg :", setg)
print("setp :", setp)

# subset or super set.
setk = {'a', 'b', 'c', 2, 6, 1}
setl = {'a', 'b'}
setr = {'a', 'b', 'd'}

print(setl.issubset(setk)) # True
print(setr.issubset(setk))  # False
print(setk.issuperset(setl))
"""

# difference_update

setk = {'a', 'b', 'c', 2, 6, 1}
setl = {'a', 'b', 'g', 'f'}

setk.difference_update(setl)
print("setk :", setk)
print("setl :", setl)


setkk = {'a', 'b', 'c', 2, 6, 1, 'y'}
setll = {'a', 'b', 'g', 'f'}

setkk.symmetric_difference_update(setll)
print("setkk :", setkk)
print("setll :", setll)

