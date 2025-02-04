f1=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test284.jpg','rb')


data=f1.read()
print(type(data))

print(data)


f2=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/imnagecopy.jpg','wb')
f2.write(data)
print('image 2 is read ')

f1.close()
f2.close()