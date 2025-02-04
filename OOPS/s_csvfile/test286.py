#read data from csv file

import csv
with open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test286.csv','r') as  f:
    r=csv.reader(f)
    print(type(r))
    data=list(r)

    print(data)
    print('..............................')
    for row in data:
        for column in row:
            print(column,'\t',end='')
        print()
    print('..............................')
    for row in data:
        print(row)
