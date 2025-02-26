def inputtodict(n):
    temp={}
    for i in range(n):
        key=input('enter the key')
        value=input('enter the value')
        temp[key]=value
    return temp


l=dict(inputtodict(3))
print(l)
