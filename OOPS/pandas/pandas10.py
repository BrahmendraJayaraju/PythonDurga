
#• marker plot
import matplotlib.pyplot as plt
import numpy as np

sick_leave_applied=np.array([4,12,2,25,22,27,30])

plt.xlabel('Number of Days')
plt.ylabel('Difference of 5 days')
plt.plot(sick_leave_applied,marker='s')
plt.show()