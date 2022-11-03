"""
pip install pandas
"""
import pandas as pd

"""
import pandas as pd

# Series : One diamentional data or array , then can use series
# DataFrame

list1 = [5, 7, 8, 'Hello', 'Python']

sr = pd.Series(list1)

print(sr)
print(sr[1])

sr2 = pd.Series(list1, index=['a', 'b', 'c', 'd', 'e'])

print(sr2)
print(sr2.shape)
print(sr2.dtype)
print(sr2.size)

print("#"*40)
dict1 = {'name' : 'Vaibhav', 'age': 45, 'salary': '1cr'}

sr3 = pd.Series(dict1)
print(sr3)

dict11 = {'name' : ['Vaibhav', 'Yogesh'], 'age': [45, 60], 'salary': ['1cr', '2Cr']}

print("#"*40)
sr4 = pd.Series(dict11)
print(sr4[0])
print(sr4['age'][0])
"""
#############################################
 # Dataframe


dict11 = {'name' : ['Vaibhav', 'Yogesh', 'Gauri'], 'age': [45, 60, 70], 'salary': ['1cr', '2Cr', '100cr']}

df = pd.DataFrame(dict11)
print(df)

"""
print(df['name'][1])
print(df['age'][1])

for data in df.items():
    print(data[1][2])

"""

#print(df['age'][2])

def get_specific_person_age(per_name='Vaibhav',  quer='salary'):
    index = 0
    for name in df['name']:
        if name == per_name:
            return df[quer][index]
        else:
            index = index + 1

#vab_age = get_specific_person_age('Gauri', 'age')
#print(vab_age)

# add new colum to the data frame
df['email'] = ['vaib@gmail.com', 'yog@gmail.com', 'gauri@gmail.com']

print(df)

# remover colum from dataframe

del df['age']
print("#"*50)
print(df)


# get each row via data frame
print("_"*20)
for data in df.iterrows():
    print(data)

#del df.iterrows()[0]
#print(df)

###########################################################

# append two data frame

user_info1 = {'name': ['a', 'b', 'c'], 'age' : [67, 87, 78]}
user_info2 = {'name': ['d', 'e', 'f', 'g'], 'age' : [56, 77, 33, 44]}

df1 = pd.DataFrame(user_info1)
df2 = pd.DataFrame(user_info2)

print(df1.append(df2, ignore_index=True))

############# drop any row from the DataFrame #################

