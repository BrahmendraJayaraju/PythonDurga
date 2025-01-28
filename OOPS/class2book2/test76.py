class outer:
    def __init__(self):
        print('thi is outer class constructor')

    class inner:
        def __init__(self):
            print('thi is inner class constructor')

        def m1(self):
            print('inner class instance method')

a=outer()
b=a.inner()
b.m1()
print()
outer().inner().m1()
