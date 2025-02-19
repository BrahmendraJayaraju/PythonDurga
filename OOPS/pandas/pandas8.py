import matplotlib.pyplot as plt
import  pandas as pd
import numpy as np



print('..........................................................')
#line plot
x=[2010,2012,2014,2016,2018]
y=[10,20,15,30,10]
plt.plot(x,y)
plt.title('Simple Line Plot')
plt.xlabel('year of hike')
plt.ylabel('% of hike')
plt.show()