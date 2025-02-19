import matplotlib.pyplot as plt
import numpy as np

#bar plot

x=np.array(['Tomato','Spinach','Nuts','Meat','Fish'])
y=np.array([40,60,120,160,200])



#to print value on labels 
for i,y in enumerate(y):
 plt.text(i,y,f"${y}",ha='center')


plt.title('Item Price')
plt.xlabel('Item')
plt.ylabel('Price($)')
plt.bar(x,y)
plt.show()
