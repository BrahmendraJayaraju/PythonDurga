from zipfile import ZipFile, ZIP_DEFLATED, ZIP_STORED

#unzip the file

#this is not working
f=ZipFile('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/test287.zip','r',ZIP_STORED)

names=f.namelist()
print(names)

for i in names:
    print(i)

    f1=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/test287/'+i,'r')
    text=f1.read()
    print('file nanme:',i)
    print('content in file:',text)
    f1.close()
    print()



print('UNzip is doen ')