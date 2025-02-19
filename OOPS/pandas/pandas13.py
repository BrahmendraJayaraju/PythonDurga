

import matplotlib.pyplot as plt
import numpy as np

#area plot
days=[1,2,3,4,5]
predicted_weather=[70,31,79,33,45]
difference_from_actual=[-1,38,12,59,25]

plt.plot([],[],color='c',label='Predicted weather',linewidth=5)
plt.plot([],[],color='g',label='Actual weather',linewidth=5)

plt.stackplot(days,predicted_weather,difference_from_actual,colors=['c','g'])

plt.xlabel('Days')
plt.ylabel('Temperature in Fahrenheit')
plt.title('Weather report using area plot')
plt.legend()
plt.show()