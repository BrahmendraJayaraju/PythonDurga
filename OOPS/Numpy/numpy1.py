#creating one dimensional array
import numpy as np

one_array=np.array([4,2,3])
print(one_array)
print(type(one_array))

print(".............................................")
#creating 2 dimensional array

two_array=np.array([[4,2,3],[5,6,7]])
print(two_array)
print(type(two_array))

print(".............................................")


#creating multi dimensional array

multi_array=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[45,67,88]]])
print(multi_array)

print(".............................................")


#check the dimensions of the array
a_one=np.array(42)
a_two=np.array([1,2,3,4,5])
a_three=np.array([[4,5,6],[7,8,9]])
a_four=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a_one.ndim)
print(a_two.ndim)
print(a_three.ndim)
print(a_four.ndim)


print(".............................................")

#numpy functions
#finding the shape of given array

arr=np.array([[10,20,30,40],[50,60,70,80]])

print(arr.shape)


print(".............................................")
#reshape the array valid

arr1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr1.reshape(4,3)
print(newarr)

print(".............................................")
#reshape the array in valid

arr1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#newarr=arr1.reshape(4,4)
print(newarr)

print(".............................................")

ar3=np.array([3,5,6])
ar4=np.array([8,9,0])
mer=np.concatenate((ar3,ar4))
print(mer)