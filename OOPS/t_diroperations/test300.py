import os
from datetime import *


s=os.stat('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test299.txt')
print('file size:',s.st_size)
print('last modified',s.st_mtime)

#time we need to convert in proper format

a=datetime.fromtimestamp(s.st_mtime)
print(a)