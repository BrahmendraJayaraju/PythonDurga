f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test266.txt','w')


#dict
#only keys will be added
l={'durge\n':100,'ravi\n':200,'brahmendra\n':212720597}

f.writelines(l)
f.close()
print('data is written ')