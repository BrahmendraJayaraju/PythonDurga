f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test281.txt', 'w')


f.write('ALL STUDENTS ARE STUPIDS')

with open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test281.txt','r+') as f:
    text=f.read()
    print('data before modification')
    print(text)
    print('current cursor position is at :',f.tell())
    f.seek(17)
    f.write('gems!!!')
    f.seek(0)
    text=f.read()
    print('data after modification')
    print(text)






