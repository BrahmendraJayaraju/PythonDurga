#to get proper names


import os

g=os.walk('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/cwd')


for dirpath,dirname,filename in g:
    print('directory path:',dirpath)
    print('...........')
    print('directory name:', dirname)
    print('...........')
    print('directory file name:', filename)
    print('...........')