#to count down from 5
import time


def count_down(n):
    while n>=1:
        yield n
        n=n-1

g=count_down(5)

for x in g:
    print(x)
    time.sleep(1)