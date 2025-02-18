
import numpy as np

print('........................................')

books=np.array(['physi','ds','mat','pyth','hadoo','oop','jav','clo'])
print(books[5:])

print('........................................')

x=np.array([8,7,6,5,9,3,2,1])
print(x[1:6:3])
print(x[::5])


print('........................................')
#neg slic
neg_lice=np.array([13,34,58,69,44,56,37,24])

print(neg_lice[::-1])

print(neg_lice[:-1])