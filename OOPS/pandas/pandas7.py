import  pandas as pd
import numpy as np



print('..........................................................')

#convert to lower
text=pd.Series(['Animals','PLANTS','Mammals','Substances','Algae','FUNGUS'],dtype='string')
print(text.str.lower())

print('..........................................................')
#convert to upper
print(text.str.upper())

print('..........................................................')

print(text.str.len())

print('..........................................................')


#plotting with pandas  and matplot
import matplotlib.pyplot as plt
df=pd.read_csv('results.csv')
df.plot()
plt.show()