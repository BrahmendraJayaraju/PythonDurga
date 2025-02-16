def decor1(func):
    def inner1():
        print('decor1 execution')
    func()
    return inner1

def decor2(func):
    def inner2():
        print('decor2 execution')

    return inner2


@decor2
@decor1
def f():
    print('original function')

f()
