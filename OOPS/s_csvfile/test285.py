#to create csv and enter data to csv file

import csv
with open('/files/test286.csv', 'w') as  f:
    w=csv.writer(f)
    w.writerow(['eno','ename','esal','eadhar'])
    while True:
        eno=int(input('enter the eno:'))
        ename = input('enter the ename:')
        esal = int(input('enter the esal:'))
        eadhar = int(input('enter the eadhar:'))

        w.writerow([eno,ename,esal,eadhar])
        option=input('do you want to continue:')
        if option.lower()=='no':
            break
print('done')