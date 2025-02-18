print('..................................................')

import  pandas as pd
import numpy as np

oly={'hospitality':['london','beijing','athens','sydney','atlanta'],'year':['2012','2008','2004','2000','1996'],'no of participants':['205','204','201','200','197']}

a1=pd.DataFrame(oly)
print(a1)


print('....................................................................')

#import data from sql

#df=pd.read_sql_query('select * from employee',conn)


print('....................................................................')

#create dataframe from dict

olyd={'beijing':{2008:204},'london':{2012:205}}
dfoly=pd.DataFrame(olyd)

print(dfoly)

print('....................................................................')
#to view the dataframe

print('using the describe function to view the dataframe')

print(a1.describe())


print('....................................................................')

#only to get host city details

print('to get host city details :')

print(a1.hospitality)