def gcd():
    m,n=0,1
    while n!=0:
        if m>n:
            m=m-n
        else:
            n=n-m
    value=m
    print("gcd is ",value)
print(gcd)
print('function call yet')
gcd()
print('function call happened')
print('-'*30)







        
