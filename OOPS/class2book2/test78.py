class outer:
    def __init__(self):
        print('thi is outer class constructor')

    class inner_1:
        def __init__(self):
            print('thi is inner_1 class constructor')

        class inner2:
            def __init__(self):
                print('thi is inner_2 class constructor')

            @staticmethod
            def m1():
                print('inner class instance method')

a=outer()
b=a.inner_1()
c=b.inner2()
c.m1()
print()

#using object creation
outer().inner_1().inner2().m1()
print()
#using class name
outer().inner_1().inner2.m1()