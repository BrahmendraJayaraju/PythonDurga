import numpy as np


#calculate the average of the given array element

a=np.array([[2,3,4],[3,6,7],[5,7,8]])
b=np.average(a,axis=0)
print(b)
print('........................................')

#calculating min and max of the array element

v=np.array([1,8,3])
print(v.max())
print(v.min())

print(min(v))
print('........................................')

#numpy miscelleneous functions
y=np.linspace(15,30,10)

print(y)
print('........................................')

#random value between 0 and 1

import random
n=random.random()
print(n)

print('........................................')
#next
print('number from normal distribution with 0 and sd 1')

print(np.random.randn(5,3))

print('........................................')

print('........................................')
#next

random1=np.random.randint(1,10)
print('random numbers b/w one and ten is:',random1)
print('random numbers between specified range:')
print(np.random.randint(1,50,(2,2)))

print('........................................')
#next transpose

a=np.array([[1,2],[4,5],[7,8]])
print(a)
b=np.transpose(a)
print(b)

