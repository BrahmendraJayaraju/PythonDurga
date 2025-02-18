

print('..................................................')

import  pandas as pd
import numpy as np

s=pd.Series(np.random.rand(4))
print('is  the object empty: ')
print(s.empty)
print(s)


print('..................................................')

#check dimension

s=pd.Series(np.random.rand(5))
print(s)
print('the dimension of the object ',s.ndim)


print('..................................................')

#size function

s=pd.Series(np.random.rand(6))
print(s)
print('the size of the object:',s.size)

print('..................................................')

s=pd.Series(np.random.rand(6))
print(s)
print('the actual data series is:')
print(s.values)


print('..................................................')
#head function
s=pd.Series(np.random.rand(6))
print('the original series is:')
print(s)

print('the first three rows of the data series')
print(s.head(3))

print('..................................................')
#tail function
s1=pd.Series(np.random.rand(6))
print('the original series is:')
print(s1)

print('the last three rows of the data series')
print(s1.tail(3))

print('..................................................')

