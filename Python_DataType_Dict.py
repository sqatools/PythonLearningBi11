#dict1 = {'key': 'value'}

dict1 = {'name': 'Rahul', 'age': 25, 'address': 'Pune'}

print(dict1, type(dict1))

print(dict1['name'])

print(dict1['address'])

dict1['mobile'] = [567345, 634545665, 354656567]

print(dict1)

print(dict1['mobile'][1])

school = {
    'student' : {
       'stud1' : {'name': 'st1', 'email': 'email1@test.com', 'mobile': 345643545},
       'stud2' : {'name': 'st2', 'email': 'email2@test.com', 'mobile': 3454543536},
       'stud3' : {'name': 'st3', 'email': 'email3@test.com', 'mobile': 345634543},
    },
    'teacher': {
        'teach1' : {'name': 'teach1', 'email': 'email11@test.com', 'mobile': 34588643545},
        'teach2' : {'name': 'teach2', 'email': 'email12@test.com', 'mobile': [3448643545, 54355434]}
    }
}

print(school['teacher']['teach2']['mobile'][1])

school1 = {
    'student' : [
        [
         {'name': 'st1', 'email': 'email1@test.com', 'mobile': 345643545},
         {'name': 'st2', 'email': 'email2@test.com', 'mobile': 3454543536},
         {'name': 'st3', 'email': 'email3@test.com'}]
    ],
    'teacher': {
        'teach1' : {'name': 'teach1', 'email': 'email11@test.com', 'mobile': 34588643545},
        'teach2' : {'name': 'teach2', 'email': 'email12@test.com', 'mobile': [3448643545, 54355434]}
    }
}

print(school1['student'][0][2]['name'])

"""
Properties:

1. Dict is mutable data type.
2. Dict is unstructure data type and it does not follow any indexing
3. Dict can contain only unique key, duplicate key is not allowed.
4. Only immutable data type can be key in the dictionary int, float, string, tuple.
5.  We can assign any type of data as value in the dictionary.
6. Dictionary store data in form of key value pair.
"""

print("___"*30)

#print(dict11)

dict11 = {'a': 123}

#dict11[[345, 567]] = 'Python'

dict11[(345, 567)] = 'Python'

print(dict11)


dicta = {'a': 567, 'b': 123, 'c': 222, 'b': 444}

print(dicta)