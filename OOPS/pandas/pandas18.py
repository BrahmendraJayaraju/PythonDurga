import matplotlib.pyplot as plt
import numpy as np

#pie plot

plt.title('Population rate in 2010')
y=np.array([45,25,35,24,10,15])
labels=['newyork','texas','india','china','srilanka','malaysia']
plt.pie(y,labels=labels,explode=(0,0,0.2,0,0,0),autopct='%1.1f%%',shadow=True,startangle=150)

plt.show()