def inputtolist(n):
    temp=[]
    for i in range(n):
        value=int(input('enter the value'))
        temp.append(value)
    return temp

    
l=inputtolist(3)
print(l)
