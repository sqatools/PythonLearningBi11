import pandas as pd

data = {'name': ['rahul', 'mohit', 'mehul'], 'city': ['mumbai', 'Pune', 'Kolkata']}
data2 = {'name': ['rahul1', 'mohit2', 'mehul3'], 'city': ['solarput', 'Ahemdabad', 'Hyderabad']}

df1 = pd.DataFrame(data)
print(df1)
df2 = pd.DataFrame(data2)
print(df2)

output = df1 + df2
print(output)


