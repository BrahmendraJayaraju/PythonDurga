#0,1,1,2,3,5  fibonacci

import time
def fibo():
    a,b=0,1  #initialize
    while True:
        yield a
        a,b=b,a+b  #update


g=fibo()

for x in g:
    print(x)
    time.sleep(1)