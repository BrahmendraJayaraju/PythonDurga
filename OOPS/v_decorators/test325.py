def decor(func):
    def inner(name):
        n=['CM','PM','MINISTER']
        if name in n:
            print('#'*50)
            print('good morning {} have a great day'.format(name))
            print('#'*50)
        else:
            func(name)
    return inner

@decor
def wish(name):
    print('good morning:',name)


wish('durge')
wish('PM')
wish('sunny')
wish('CM')
