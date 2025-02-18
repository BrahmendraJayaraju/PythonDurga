
import  pandas as pd
import numpy as np
df=pd.read_csv('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/OOPS/pandas/results.csv')

print('....................................................................')


#to get 1 sample data of 1 record
# to get 10
print(df.sample())
print(df.sample(10))

print('....................................................................')

#to get info of dataframe

print(df.info())

print('....................................................................')

#getting the  statistical information of data set

print(df.describe())

print('....................................................................')
#we can query

print(df.query('away_score>2'))


print('....................................................................')
#we can query using condition

print(df.query('away_score>2' and 'home_score>4'))


print('....................................................................')
#we can query using string

print(df.query('country.str.contains("England")'))


print('....................................................................')
#to get only unique city

print(df['city'].unique())

print('....................................................................')
#to check nul values
print(df.isnull())