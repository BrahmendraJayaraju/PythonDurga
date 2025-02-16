def decor(func):
    def inner(name):
        if name=='sunny':
            print('#'*50)
            print('hello sunny ,you are very important for us')
            print('very very gm')
            print('#'*50)
        else:
            func(name)
    return inner

@decor
def wish(name):
    print('good morning:',name)


wish('durge')
print('........................')
wish('sunny')
