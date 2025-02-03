f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test263.txt','w')


#list data
l=['listdata','ML\n','AI\n','GENERATIVE AI\n','DS\n']

f.writelines(l)
f.close()
print('data is written ')