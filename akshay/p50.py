def inputtotuple(n):
    temp=[]
    for i in range(n):
        value=int(input('enter the value'))
        temp.append(value)
    return temp

l=tuple(inputtotuple(4))
print(l)
    
