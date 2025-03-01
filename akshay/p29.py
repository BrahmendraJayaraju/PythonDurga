def gcd():
    m,n=1,0
    if m == 0:
       value=n
    else:
        while n != 0:
            if m > n:
                m = m - n
            else:
                n = n - m
        value = m
    print("gcd is ", value)



print(gcd)
print('function call yet')
gcd()
print('function call happened')
print('-'*30)







        
