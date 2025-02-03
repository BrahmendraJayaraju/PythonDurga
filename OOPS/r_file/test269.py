#to write dynamic data to file



fname=input('enter the file name:')
f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/'+fname,'w')

while True:
    data=input('enter the dat to write :')
    f.write(data+'\n')
    option=input('do you want to add some more data:')
    if option.lower()=='no':
        break

f.close()
print('data write and close')

