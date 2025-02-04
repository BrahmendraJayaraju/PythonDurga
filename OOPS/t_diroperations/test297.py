#to get complete list of folders and file names

import os

g=os.walk('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/cwd')

for x in g:
    print(x)
