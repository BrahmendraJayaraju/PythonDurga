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
#this will not work  it is not possible

dataframe=pd.read_csv('housing_data.csv',index_col=0)
numerical_feature_columns=list(dataframe._get_numeric_data().columns)
dataframe1=numerical_feature_columns

plt.figure(figsize=(12,8))
sns.heatmap(dataframe1.corr(),cmap='viridis')


#--next--------------------------------------------------------------