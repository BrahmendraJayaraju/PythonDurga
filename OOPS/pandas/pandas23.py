#--next--------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Plotting a Hex Plot

dataframe=pd.read_csv('housing_data.csv',index_col=0)
sns.jointplot(x='YearBuilt',y='SalePrice',data=dataframe,kind='hex')

plt.show()

#--next--------------------------------------------------------------
#Plotting a Heatmap

#this will not work  it is not possible skip this

#dataframe=pd.read_csv('housing_data.csv',index_col=0)
#numerical_feature_columns=list(dataframe._get_numeric_data().columns)
#dataframe1=numerical_feature_columns

#plt.figure(figsize=(12,8))
#sns.heatmap(dataframe1.corr(),cmap='viridis')


#--next--------------------------------------------------------------
#Plotting a Pair Plot

import seaborn as sns
cols=['SalePrice','OverallQual','GrLivArea','GarageCars','TotalBsmtSF','FullBath','YearBuilt']

sns.pairplot(dataframe[cols])
plt.show()


#--next--------------------------------------------------------------
#Plotting Numeric vs Categorical Data
#Plotting a box plot

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dataframe=pd.read_csv('housing_data.csv',index_col=0)
plt.figure(figsize=(15,8))
plt.xticks(rotation=45)

sns.boxplot(x='Neighborhood',y='SalePrice',data=dataframe)
plt.show()
