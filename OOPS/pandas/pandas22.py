#--next--------------------------------------------------------------
#• Plotting a Y-Axis Oriented Count Plot
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dataframe=pd.read_csv('housing_data.csv',index_col=0)
sns.countplot(y='Neighborhood',data=dataframe)
plt.show()

#--next--------------------------------------------------------------
#Plotting Numeric vs Numeric Data

#linear model plot
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dataframe=pd.read_csv('housing_data.csv',index_col=0)

sns.lmplot(x='GrLivArea',y='SalePrice',data=dataframe,fit_reg=True)
plt.show()


#--next--------------------------------------------------------------
#Plotting a Joint Plot

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.jointplot(x='TotalBsmtSF',y='SalePrice',data=dataframe,kind='reg')
plt.show()


