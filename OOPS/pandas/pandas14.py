import matplotlib.pyplot as plt
import numpy as np

#subplot

x1=np.array([2000,2010,2020,2030])
y1=np.array([6,3,12,10])

plt.subplot(1,2,1)
plt.plot(x1,y1)

x2=np.array([2000,2010,2020,2030])
y2=np.array([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x2,y2)
plt.show()