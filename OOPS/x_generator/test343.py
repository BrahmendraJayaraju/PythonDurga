##0,1,1,2,3,5  fibonacci numbers  less than 10


import time
def fibo():
    a,b=0,1  #initialize
    while True:
        yield a
        a,b=b,a+b  #update


g=fibo()

for x in g:
    if x<=10:
       print(x)
       time.sleep(1)