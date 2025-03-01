

def inputheterolist(n):
    temp=[]
    for i in range (n):
        
        datatype=input('enter the datatype:')
        datatype=datatype.lower()
        
        if datatype.startswith('int'):
           value=int(input('enter the value'))
            
        elif datatype.startswith('float'):
             value=float(input('enter the value'))
            
        elif datatype.startswith('bool'):
             value=bool(input('enter the value'))
            
        elif datatype.startswith('complex'):
             value=complex(input('enter the value'))
            
        elif datatype.startswith('str'):
             value=input('enter the value')

        elif datatype.startswith('list'):
             listnumber=int(input('enter the how many list number'))
             value=inputtolist(listnumber)

        elif datatype.startswith('set'):
             setnumber=int(input('enter the how many set number'))
             value=inputtoset(setnumber)

        elif datatype.startswith('tuple'):
             tuplenumber=int(input('enter the how many tuple number'))
             value=inputtotuple(tuplenumber)

        elif datatype.startswith('dict'):
             dictnumber=int(input('enter the how many dict number'))
             value=inputtodict(2)
            
        else:
             print('invalid data type')
             value=None
        temp.append(value)        
    return temp



def inputtolist(n):
    temp=[]
    for i in range(n):
        value=int(input('enter the value'))
        temp.append(value)
    return temp


def inputtoset(n):
    temp=set()
    for i in range(n):
        value=int(input('enter the value'))
        temp.add(value)
    return temp


def inputtotuple(n):
    temp=[]
    for i in range(n):
        value=int(input('enter the value'))
        temp.append(value)
    return tuple(temp)

def inputtodict(n):
    temp={}
    for i in range(n):
        key=input('enter the key')
        value=input('enter the value')
        temp[key]=value
    return dict(temp)


print(inputheterolist(3))








