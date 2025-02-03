f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test265.txt','w')


#set order not followed
l={'sunny\n','bunny\n','chinny\n','vinny\n'}

f.writelines(l)
f.close()
print('data is written ')