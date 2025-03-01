

def split(str):
    temp=''
    a1=[]
    for i in str:

        if i!=' ':
            temp=temp+i

        else:
            a1.append(temp)

            temp=''
    if temp:
        a1.append(temp)

    return a1


a=split(str(input('enter the string:')))
print(a)