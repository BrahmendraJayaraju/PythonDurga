import matplotlib.pyplot as plt
import numpy as np

#histogram

data=np.random.normal(134,20,250)


print(data)
print(len(data))
plt.hist(data)
plt.show()