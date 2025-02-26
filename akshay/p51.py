def inputtoset(n):
    temp=[]
    for i in range(n):
        value=int(input('enter the value'))
        temp.append(value)
    return temp

l=set(inputtoset(3))
print(l)
        
