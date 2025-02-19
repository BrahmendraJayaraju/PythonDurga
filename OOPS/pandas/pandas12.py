import matplotlib.pyplot as plt
import numpy as np


#grid plot
b1=np.array([80,85,90,95,100,105,110,115,120,125])
b2=np.array([240,250,260,270,280,290,300,310,320,330])
plt.plot(b1,b2)
plt.title('Diet Chart')
plt.xlabel('Protiens Intake')
plt.ylabel('Calorie Burnage')
plt.grid()
plt.show()