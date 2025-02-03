f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test274.txt','r')

#to get values in list form  on beow other like in file

l=f.readlines()

for line in l:
    print(line,end='')


f.close()
