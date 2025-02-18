

#creating  empty series

import pandas as pd
from contourpy.util.data import simple

from OOPS.v_decorators.test321 import list1

empty=pd.Series()
print(empty)

print('..................................................')

#creating a series from an array
import numpy as np

var=np.array(['ab','cd','ef','gh','s'])
simple=pd.Series(var)
print(simple)

print('..................................................')
#creating a series from an  list
list=['hello','welcome','python','pandas','a','b']

var=pd.Series(list)
print(var)

print('..................................................')

#creating a series from an  dict

dict={'welcome':10,'to':40, 'learn':70}

var=pd.Series(dict)
print(var)

print('..................................................')


var=pd.Series(30,index=[0,1,2,3,4,5])

print(var)



