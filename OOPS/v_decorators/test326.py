


def smart_division(func):
    def inner(a,b):
        if b==0:
            print('monkey we can divide by zeo')
        else:
            func(a,b)
    return inner


@smart_division
def division(a,b):
    print(a/b)
    
division(10,0)
division(10,2)
