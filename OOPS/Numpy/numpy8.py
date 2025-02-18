import numpy as np

print('........................................')
#a range
print('numbers:',type(np.arange(2,10)))
np.arange(2,10,1.2)

print('........................................')
#indexing

x=np.array(['math','sci','che','compu'])
print(x[3])

print('........................................')

y=np.array([[10,20,30,40,50],[60,70,80,90,100]])

print('4th element 1st row :',y[0,3])

print('........................................')

index=np.array([121,235,353,254])
print(index[1]+index[0])


print('........................................')

y=np.array([[[5,6,36],[44,65,67]],[[47,78,59],[10,21,42]]])
print(y[0,1,2]-y[0,1,1])




