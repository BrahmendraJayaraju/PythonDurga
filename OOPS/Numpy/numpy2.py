#numpy  airthemitic functions


#addition and subtra
import numpy as np
a=np.array([30,20,10])
b=np.array([10,20,30])

result=np.add(a,b)
print("addition:",result)

result1=np.subtract(a,b)
print(result1)


print(".....................................")
# multi and division
c=np.array([50,70,10])
d=np.array([10,20,40])

result3=np.multiply(c,d)
result4=np.divide(c,d)
print(result3)
print(result4)

print(".....................................")

#floor division

result5=np.floor_divide(c,d)
print(result5)

print(".....................................")
# power
x=[2,2,2,2,2]
y=[2,3,4,5,6]
z=np.power(x,y)
print(z)

print(".....................................")

#modulus
m1=np.array([20,40,70])
m2=np.array([10,30,40])
resultm=np.mod(m1,m2)
print(resultm)