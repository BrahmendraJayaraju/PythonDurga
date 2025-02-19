
import  pandas as pd
import numpy as np
df=pd.read_csv('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/OOPS/pandas/results.csv')

print('....................................................................')
#to check count

print(df.isnull().sum())

print('....................................................................')

#datetime and timedelta in pandas

df=pd.DataFrame({'date':['2/1/2001','3/7/2000','3/02/2000'],'value':[6,3,8]})
df['date']=pd.to_datetime(df['date'])
print(df)

print('....................................................................')
#to get current date month


from datetime import date
today=date.today()
print(today)

print('current year:',today.year)
print('current month',today.month)
print('current day',today.day)



print('....................................................................')
#using the time data functions

print(pd.to_timedelta('5 days 3 hours 58 minutes 10 seconds'))