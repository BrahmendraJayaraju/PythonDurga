#we can pass a function argument to another function


def f1(func):
    func()

def f2():
    print('f2 function')


f1(f2)