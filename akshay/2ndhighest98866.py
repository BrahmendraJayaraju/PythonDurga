def greatlist(n):
    temp=[]
    for i in range(n):
       a=int(input('enter the numbers'))
       temp.append(a)
    return temp

def greatestnumber():
    n=int(input('enter the total numbers:'))
    data=greatlist(n)
    great=data[0]

    for i in range(0,n):
        if data[i]>great:
            great=data[i]

    print('first great:',great)
    secgreat=float('-inf')
    for i in range(0,n):
       if data[i]!=great:
           if data[i] > secgreat:
             secgreat = data[i]

    return secgreat




print(greatestnumber())