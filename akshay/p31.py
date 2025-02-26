def gcd(m,n):
    while n!=0:
        if m>n:
            m=m-n
        else:
            n=n-m
    value=m
    print('gcd is',value)

print(gcd)
print('function call')
a,b=10,20
gcd(10,20)
print('function call happened')
