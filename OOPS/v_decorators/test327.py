#how to call same function with decorator and without decorator


def decor(func):
    def inner(name):
        if name=='sunny':
            print('#'*50)
            print('hello sunny you are important')
            print('very very good morning')
            print('#'*50)
        else:
            func(name)
    return inner

def wish(name):
    print('good mornng:',name)



d1=decor(wish)

wish('durga')
wish('sunny')


print('#####################')
d1('durga')
d1('sunny')
