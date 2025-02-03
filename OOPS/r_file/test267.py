f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test267.txt','w')


#dict
#only keys will be added
l={'mohan\n':100,'yurb\n':200,'brahmendra\n':212720597}

f.writelines(l)
#to store  values
#int to be converted to str 
f.writelines(str(l.values()))

f.close()
print('data is written ')