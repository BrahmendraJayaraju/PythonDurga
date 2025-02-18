import  pandas as pd
import numpy as np

print('....................................................................')

#data frame functions

#getting basic information about data set
df=pd.read_csv('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/OOPS/pandas/results.csv')

print(df.head(5))

print('....................................................................')
#to get whole data
print(df)



print('....................................................................')
#to get last 7  data
print(df.tail(7))

print('....................................................................')
