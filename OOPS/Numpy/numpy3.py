import numpy as np


#numpy string functions
#adding string
a=np.array(['hello','welcome'])
b=np.array(['world','learners'])

result=np.char.add(a,b)
print(result)


print("...........................................")
# replace string

str='hello how are you'
print(str)
a=np.char.replace(str,'hello','hi')
print(a)


print("...........................................")

#convert string to lower and upper cases

x='hello how are you'
print(x)
up=np.char.upper(x)
print(up)

y='GREETING OF THE DAY'
print(y)
lp=np.char.lower(y)
print(lp)

print("...........................................")