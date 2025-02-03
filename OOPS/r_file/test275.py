f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test274.txt','r')

#quiz

print(f.read(3))

print(f.readline())
#bse \n spacce
print(f.readline())

print(f.read(4))
print('reamiming data:')
print(f.read())

f.close()