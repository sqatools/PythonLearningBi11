# define empty dictionary
# dict  = {key : value}

dict1 = {'name': 'rahul'}

print(dict1, type(dict1))

dict2 = {}
dict3 = dict()
print(type(dict2), dict3, type(dict3))

list1 = list()  # Empty  list
list2 = []      # Empty list
list3 = [5]      # list with single value

print("list1 :", list1, type(list1))
print("list2 :", list2, type(list2))
print("list3 :", list3, type(list3))

tupl1 = tuple()  # Empty Tuple
tupl2 = (4,)  # Tuple with single value, we have put comma after first value
tupl3 = ()  # Empty Tuple

print("tupl1 :", tupl1, type(tupl1))
print("tupl2 :", tupl2, type(tupl2))
print("tupl3 :", tupl3, type(tupl3))

str1 = str()

#

"""
-> dict contains key value pair
-> Only immutable data type can be key in the  dict, e.g int, float, string, tuple
-> All type of data can be value in the dictionary, int, float, string, list, tuple dict
-> Duplicate key is not allowed in the dict, if duplicate key is given then latest key value 
   will be considered.
"""

# Create a dictionary and add/update the data in the dict.

employee = {'emp_name': 'renuka'}

employee['salary']  = 1200000  # add new data in the dict
print(employee)

employee['emp_name'] = 'Renuka Gogekar'
print(employee)

fake_data = {}

for i in range(1, 1001):
    fake_data[f'emp_id_{i}'] = f'emp_tcs_{i}'

print(fake_data)

# Generate a fakedata with dictionary
# Main dict name is will be TCS
# This company will have department (HR, Support, Development, Testing)
# Each department has 50 users
# Each user has their own general information (name, salary, email, mobile, address)

"""
TCS = {
    'HR' : [{'name': 'name1',  'email': 'emailid', 'mobile': 54646454, }],
    'Support' : [{'name': 'name1',  'email': 'emailid', 'mobile': 54646454}],
    'Development' : [{'name': 'name1',  'email': 'emailid', 'mobile': 54646454, }],
    'Testing' : [{'name': 'name1',  'email': 'emailid', 'mobile': 54646454, }],
}

TCS = {}

TCS['HR'] = [{"name": 'user1'}]
TCS['Support'] = [{"name": 'user1'}]
TCS['Development'] = [{"name": 'user1'}]
TCS['Testing'] = [{"name": 'user1'}]

print(TCS)
"""
# Check any data is available in the dict or not
"""
dict1 = {'a': 456, 'b': 345, 'c': 123}
num = 'd'

if num in dict1:
    print(True)
else:
    print(False)

output = num in dict1
print(output)
"""




# apply loop on the dictionary

"""
dict1 = {'a': 456, 'b': 345, 'c': 123}

# This loop will return keys of the dictionary
for data in dict1:
    print(data)

# Get key value pair with tuple as in the loop, we can use items
for data in dict1.items():
    print(data)

# Get key value pair separate var as in the loop, we can use items
for k, v in dict1.items():
    print("key :", k, "value:", v)


# write a python program to print below output

str1 = "Hello Good Morning"
output1 = {"_H_" : "H-e-l-l-0", "_G_" :  "G-o-o-d", "_M_": "M-o-r-n-i-n-g"}
output2 = {"H20" : "H%ll%0", "G2d" :  "G$$d", "M2g": "M&r&n&i&n&g"}
"""

TCS = {
    'HR' : [{'name': 'name1',  'email': 'emailid', 'mobile': 54646454, }],
    'Support' : [{'name': 'name1',  'email': 'emailid', 'mobile': 54646454}],
    'Development' : [{'name': 'name1',  'email': 'emailid', 'mobile': 54646454, }],
    'Testing' : [{'name': 'name1',  'email': 'emailid', 'mobile': 54646454, }],
}



depart_list = ['HR', 'Support', 'Development', 'Testing']

for depart in depart_list:
    for i in range(1, 5):
        if depart == 'HR':
            user_info  = {'name': f'hr_name{i}',  'email': f'hr_emaiid{i}@gmail.com', 'mobile': 54646454+i, }
        elif depart == 'Support':
            user_info  = {'name': f'sp_name{i}',  'email': f'sp_emaiid{i}@gmail.com', 'mobile': 54646454+i, }
        elif depart == 'Development':
            user_info = {'name': f'dev_name{i}', 'email': f'dev_emaiid{i}@gmail.com', 'mobile': 54646454 + i, }
        elif depart == 'Testing':
            user_info = {'name': f'test_name{i}', 'email': f'test_emaiid{i}@gmail.com', 'mobile': 54646454 + i, }
        TCS[depart].append(user_info)

# pprint module to print the dict in structure
print(TCS)
from pprint import pprint

pprint(TCS)

############# Method Belogns to dict #############