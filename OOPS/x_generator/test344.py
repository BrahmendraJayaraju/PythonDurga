##0,1,1,2,3,5  fibonacci numbers only first 10


import time
def fibo():
    a,b=0,1  #initialize
    while True:
        yield a
        a,b=b,a+b  #update


g=fibo()


count=1
while count<=10:
    print(next(g))
    count=count+1