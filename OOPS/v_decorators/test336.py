def decor1(func):
    def inner1():
        x=func()
        return x*x  #0utput 400 below becomes input here 400*400
    return inner1

def decor2(func):
    def inner2():
        x=func()
        return 2*x  #output is 400
    return inner2


@decor1
@decor2
def num():
    return 20

print(num())