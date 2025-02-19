import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd

df=pd.read_csv('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/OOPS/pandas/housing_data.csv',index_col=0)

print(df)

numerical_feature_columns=list(df._get_numeric_data().columns)

print(numerical_feature_columns)