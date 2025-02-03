#to read from one file and write in other file

f1=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test268.txt','r')

f2=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test276.txt','w')



data=f1.read()

f2.write(data)


f1.close()
f2.close()