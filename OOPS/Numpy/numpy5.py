#numpy statistical function
import numpy as np

#calculate the airthmetic mean

array=np.array([[1,2,3],[3,4,5],[4,5,6]])
print(np.mean(array))
print(np.mean(array,axis=0))
print(np.mean(array,axis=1))

print('........................................')
#calculate the airthmetic median

array=np.array([[30,65,70],[80,95,10],[50,90,60]])
print('given array is :',array)
print('apply median function:',np.median(array))
print('along columns median:',np.median(array,axis=0))
print('along  row  median:',np.median(array,axis=1))


print('........................................')

x=[10,20,7,15,34]
print('x:',x)


print('50th percentile of x:',np.percentile(x,50))
