def decor1(func):
    def inner1():
        x=func()
        return x*x
    return inner1

def decor2(func):
    def inner2():
        x=func()
        return 2*x  #output of above is 400 so 400*2
    return inner2

@decor2
@decor1
def num():
    return 20

print(num())