f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/text280.txt', 'r')

#f.seek(10,0) #goes to 10th index from there starting it prints
#f.seek(10,2)  #only zero is allowed 1,2 not allowed in python 3
f.seek(10)  #default takes 0
print(f.read())




