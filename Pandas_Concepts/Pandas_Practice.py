"""
pip install pandas
"""
import pandas as pd

"""
Series : One dimentional data
Dataframe : Multi diamentional data
"""

list1 = ['Python', 'Programming', 'Data', 'Framework']

"""
sr1 = pd.Series(list1)
print(sr1)

print(sr1[1])
"""
"""

# Series with index
sr13 = pd.Series(list1, index=['a', 'b', 'c', 'd'])
print(sr13)
print(sr13[0])

# Create dynamic indexing
list1 = ['Python', 'Programming', 'Data', 'Framework']
index_list = []
for i in range(len(list1)):
    index_list.append(f"a{i}")


print("_"*40)
print(index_list)

sr3 = pd.Series(list1, index=index_list)
print(sr3)

print(sr3['a1'])

# create series with dictionary
print("_"*50)
dict1 = {'name': 'Vaibhav', 'salary': '50Lac', 'City': 'Pune'}
dict_sr=  pd.Series(dict1)
print(dict_sr)

print(dict_sr['name'])
"""

################ DataFrame ###############
"""
name_list = ['Yogesh', 'Shabana', 'Swapnali', 'Ananda', 'Keshav']
city_list = ['Mumbai', 'Pune', 'Bangalore', 'Delhi', 'Kolkata']

name_sr = pd.Series(name_list, index=['a', 'b', 'c', 'd', 'e'])
city_sr = pd.Series(city_list, index=['a', 'b', 'c', 'd', 'e'])

dict_data = {'name': name_sr, 'city': city_sr}


# df = pd.DataFrame(dict_data)
# print(df)

df = pd.DataFrame(dict_data)
print(df)

"""
"""
###################
# Data Frame with dict data
name_list = ['Yogesh', 'Shabana', 'Swapnali', 'Ananda', 'Keshav']
city_list = ['Mumbai', 'Pune', 'Bangalore', 'Delhi', 'Kolkata']

dict_data = {'name': name_list, 'city': city_list}

df = pd.DataFrame(dict_data, index=['a', 'b', 'c', 'd', 'e'])
print(df)

print(df['name']['b'])  # Shabana

# add new colum to data frame

df['mobile'] = [56457657, 76567657, 546546456, 45654645, 464534543]
df['salary'] = [50000, 10000, 5000, 80000, 40000]
df['age'] = [40, 50, 35, 23, 25]

print(df)

# Get all the values which has age less than 4
print("_"*50)
output = df.query("age < 40")
print(output)

# Get specific person city name
print("_"*50)
city_name = df.query("name == 'Swapnali'")['city']
print(city_name)

# Delete the colum
del df['age']
print("_"*50)

print(df)

# Delete any specific row
print("_"*50)
#output = df.drop('b') # Delete single row
output = df.drop(['b', 'e']) # Delete multiple rows
print(output)

# update any specific data in the dataFrame
print("_"*50)
df['city']['c'] = 'Hyderabad'
print(df)

# Get all the which match with some pattern
print("_"*50)
output = df[df.name.str.match(r"S.*")]  # get all the name which are starting from S

print(output)


# combine data of two Dataframe

df = pd.DataFrame({'name': ['a', 'b', 'c', 'd'], 'surname': ['p', 'q', 'r', 's']})
df2 = pd.DataFrame({'name': ['a1', 'b1', 'c1', 'd1'], 'surname': ['p1', 'q1', 'r1', 's1'], 'city': ['x', 'y', 'z', 'w']})


output = df.append(df2, ignore_index=True)
print(output)
"""
################################ Add data from two colums #################


df = pd.DataFrame({'name' : ['Yogesh', 'Shabana', 'Swapnali', 'Ananda'],
                   'jan': [3000, 3200, 3455, 30670],
                   'Feb': [6565, 656545, 1026565, 226565],
                   'march': [567687, 2342234, 23432, 24324]
                   })

print(df)
print("_"*30)
total = df['Feb'] + df['march'] + df['jan']

df['total'] = total

print(df)

