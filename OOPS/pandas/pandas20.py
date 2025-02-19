
#Project Explanation
#Insurance Data Analysis




#Step 1: Import libraries such as Pandas, matplotlib, NumPy, and seaborn and load the

import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd

df=pd.read_csv('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/OOPS/pandas/insurance.csv')



print(df)


#Step 2: Check the shape of the data along with the data types of the column

print(df.shape)

print(df.dtypes)


#Step 3:Check missing values in the dataset and find the appropriate measures to fill in the missing values

print(df.isna().sum())

#Step 4: Explore the relationship between the feature and target column using a count plot of categorical columns and a scatter plot of numerical columns

fig,axs=plt.subplots(1,3,sharey=True)
df.plot(kind='scatter',x='age',y='charges',ax=axs[0],figsize=(16,8))
df.plot(kind='scatter',x='children',y='charges',ax=axs[1])
df.plot(kind='scatter',x='bmi',y='charges',ax=axs[2])

plt.xlabel('bmi')
plt.ylabel('charges')
plt.show()


import seaborn as sns
palette=['red','blue','green','yellow']
sns.countplot(data=df,x='region',palette=palette)
plt.title('Regions')
plt.show()

