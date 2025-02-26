def getelement():
    a,b=10,20
    return a,b

def add():
    a,b=getelement()
    return a+b

def main():
    sum=add()
    print('the sum is',sum)
    return

main()
