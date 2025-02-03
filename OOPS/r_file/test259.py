#w,a,rt,wt,a+,x
#all method check

f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test259.txt','x')


print('file name:',f.name)
print('file mode',f.mode)
print('is file colsed:',f.closed)


print('is file readable:',f.readable())
print('is file writable:',f.writable())
f.close()
print('is file colsed 2nd time :',f.closed)
