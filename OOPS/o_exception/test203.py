
f=None
try:
    f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/abc.txt','r')
except:
    print('some problrm with file opening')
else:
    print('file opened successfully')
    print('content of the file')
    print('#'*30)
    print(f.read())
finally:
    if f is not None:
        f.close()