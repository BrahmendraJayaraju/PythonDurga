def greatest_of_n_numbers(n):
    temp=[]
    for i in range(n):
        value=int(input('enter the value'))
        temp.append(value)
    return temp

def greatestnumber():
    n=int(input('enter the total no of elements'))
    data=greatest_of_n_numbers(n)
    great=data[0]
    for i in range (1,n):
        if data[i]>great:
            great=data[i]
    return great
