


def decor_for_add(func):
    def inner(a,b):
        print('#'*30)
        print('the sum:',end='')  #end to stay cursor in same line 
        func(a,b)
        print('#'*30)
    return inner

@decor_for_add
def add(a,b):
    print(a+b)

add(10,20)


