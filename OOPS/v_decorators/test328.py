def decor1(func):
    def inner1():
        print('this is decor1 inner1')
    return inner1


def decor2(func):
    def inner2():
        print('this is decor2 inne2')
    return inner2



@decor2  #second executed and output is decor2 output
@decor1  #first executed
def f():
    print('original function')


f()