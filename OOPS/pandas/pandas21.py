#Exploratory Data Analysis
#Univariate Analysis: Numeric Values


#--next--------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataframe=pd.read_csv('housing_data.csv',index_col=0)
numerical_feature_columns=list(dataframe._get_numeric_data().columns)
print(numerical_feature_columns)

#--next--------------------------------------------------------------
#Plotting a Histogram

import seaborn as sns
num_cols=['YearBuilt','TotalBsmtSF','GrLivArea','SalePrice']

a=len(num_cols)
print(a)
for i in range(0,len(num_cols),2):
    plt.figure(figsize=(10, 4))

    #1 row 2 colum and 1st column
    plt.subplot(121)
    sns.histplot(dataframe[num_cols[i]], kde=False)

    # 1 row 2 colum and 2nd column
    plt.subplot(122)
    sns.histplot(dataframe[num_cols[i + 1]], kde=False)

    plt.tight_layout()
    plt.show()

#--next--------------------------------------------------------------
#Plotting a Box Plot
import seaborn as sns

num_cols=['YearBuilt','TotalBsmtSF','GrLivArea','SalePrice']

for i in range(0,len(num_cols),2):
    plt.figure(figsize=(10, 4))

    plt.subplot(121)
    sns.boxplot(data=dataframe, x=num_cols[i])

    plt.subplot(122)
    sns.boxplot(data=dataframe, x=num_cols[i + 1])

    plt.tight_layout()
    plt.show()


#--next--------------------------------------------------------------
#Univariate Analysis: Categorical Values
#• Plotting an X-Axis Oriented Count Plot


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dataframe=pd.read_csv('housing_data.csv',index_col=0)

sns.countplot(x=dataframe['SaleCondition'])

plt.show()

#--next--------------------------------------------------------------