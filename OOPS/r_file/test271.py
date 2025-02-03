#use 270 file

f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test270.txt','r')


#only 10 characters are printed

#0 to 9 include \n also
data=f.read(10)

#only how much present that much printed
#data=f.read(100000)
#data=f.read(-10)  it print all foe neg

print(data)

f.close()