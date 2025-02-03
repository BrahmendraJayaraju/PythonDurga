

f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test272.txt','r')


#\n will give space so use end
line1=f.readline()
print('first line data:',line1,end='')

line2=f.readline()
print('2nd line data:',line2)

line3=f.readline()
print('3rd line data:',line3)

f.close()
