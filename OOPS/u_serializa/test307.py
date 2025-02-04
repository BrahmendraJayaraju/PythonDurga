import pickle
from test306 import employee

#multiple object serialization
f=open('emp.ser','wb')
while True:
    eno = int(input('enter eno:'))
    ename = input('enter ename:')
    esal = int(input('enter esal:'))
    eaddress = input('enter the  address:')

    e = employee(eno, ename, esal, eaddress)
    pickle.dump(e, f)

    option = input('do you want to continue:')
    if option.lower()=='no':
        break

print('multiple employee object serialization is done ')