#• Plotting a Stacked Bar Chart
#• Plotting a Stacked Bar Chart

import matplotlib.pyplot as plt
import pandas as pd
dataframe=pd.read_csv('housing_data.csv',index_col=0)

crosstab=pd.crosstab(index=dataframe['Neighborhood'],columns=dataframe['OverallQual'])

crosstab.plot(kind='bar',figsize=(12,8),stacked=True,colormap='Paired')
plt.show()

#--next--------------------------------------------------------------
import pandas as pd

a=len(dir(pd))
print(a)
print(dir(pd))
#--next--------------------------------------------------------------
import matplotlib.pyplot as plt

b=len(dir(plt))
print(b)
print(dir(plt))

#--next--------------------------------------------------------------

import numpy as np


c=len(dir(np))
print(c)
print(dir(np))


