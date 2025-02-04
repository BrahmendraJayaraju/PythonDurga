import os
#wa p to chcek the given file exists or not if it is available then print its content 
fname=input('enter file name:')

if os.path.isfile('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/'+fname):
    print('this file exists:',fname)
    f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/'+fname,'r')
    text=f.read()
    print('the content of file is :')
    print('*'*40)
    print(text)
    print('*' * 40)
    f.close()
else:
    print('file not available',fame)







