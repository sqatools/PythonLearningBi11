import pandas as pd

# Drop Rows from DataFrame
"""
dict11 = {
          'name': ['Vaibhav', 'Yogesh', 'Gauri', 'user1', 'user2'],
          'age': [45, 60, 70, 80, 40],
          'salary': ['1cr', '2Cr', '100cr', '50cr', '60cr'],
          'email': ['var@gmail.com', 'yog@gmail.com', 'guari@gmail.com', 'user1@yahoo.com', 'user2@yahoo.com']
}

df = pd.DataFrame(dict11, index=['p', 'q', 'r', 's', 't'])

print(df)

print("#"*50)

#updated_df = df.drop('r')
updated_df = df.drop(['r','t'])

print(updated_df)
"""

############################################################
# apply query on dataFrame
dict22 = {
          'name': ['Vaibhav', 'Yogesh', 'Gauri', 'user1', 'user2'],
          'age': [45, 60, 70, 80, 40],
          'salary': ['1cr', '2Cr', '100cr', '50cr', '60cr'],
          'email': ['var@gmail.com', 'yog@gmail.com', 'guari@gmail.com', 'user1@yahoo.com', 'user2@yahoo.com']
}

df = pd.DataFrame(dict22)

print(df)

print("_"*30)
#df.query("salary == '100cr'", inplace=True)
#df.query("age > 50", inplace=True)

#df.query("age > 60" and "salary == '50cr'", inplace=True)
#df.query("age > 60" or "salary == '50cr'", inplace=True)
# data = df.query("age > 60" or "salary == '50cr'")
# print(data)
print("#"*50)

#age = df.query("name == 'Vaibhav'")['age']
#print(age)
print("#"*50)
# output = df[df.name.str.match('u.*')]
#print(output)
#int