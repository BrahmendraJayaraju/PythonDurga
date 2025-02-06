def outer():
    def inner():
        print('inner function execution')

    print('inner address',inner)
    return inner

f1=outer()
f1()
f1()

print('f1 address',f1)
print('outer address',outer)


