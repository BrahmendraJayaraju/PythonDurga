def outer():
    print('outer function execution started')
    def inner():
        print('inner function')
    inner()
    print('outer function execution completed')

outer()

#inner()    #error cant call