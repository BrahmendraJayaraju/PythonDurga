def gcd(m,n):
    if m==0:
        return n
    if n==0:
        return m
    while n!=0:
        if m>n:
            m=m-n
        else:
            n=n-m
    return m


print(gcd(0,1))
