import numpy as np


#sort

x=np.array([[1,4,2,3],[9,13,61,1],[43,24,88,22]])

print(x)

print('sorted array:')
y=np.sort(x)
print(y)

print('........................................')
#sort desc order only 1 dim is possible

a1=np.array([1,4,2,3])
print(a1)
z=np.sort(a1)[::-1]
print('desc order:',z)


print('........................................')
#add col wise

a=np.array([1,2,3])
b=np.array(['a','b','c'])

c=np.stack((a,b),axis=0)

print('........................................')
#col major order

x=np.array([[1,3,5],[11,35,56]])
y=np.ravel(x,order='F')

print(y)

#row majo order
y1=np.ravel(x,order='C')

print(y1)

#KEEPING ORIGINAL ORDER
y2=np.ravel(x,order='K')

print(y2)