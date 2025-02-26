#--next--------------------------------------------------------------
#Plotting a Swarm Plot

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

dataframe=pd.read_csv('housing_data.csv',index_col=0)
plt.figure(figsize=(12,6))

sns.swarmplot(x='OverallQual',y='SalePrice',data=dataframe,hue='OverallQual',size=4)
plt.show()

#--next--------------------------------------------------------------
#Plotting Categorical Vs Categorical Data
# Checking the Relationship between the columns using crosstab() function

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

dataframe=pd.read_csv('housing_data.csv',index_col=0)

crosstab=pd.crosstab(index=dataframe['Neighborhood'],columns=dataframe['OverallQual'])
print(crosstab)