#from child classmethod how to call parent class constructor and instance method indirectly

class p:
    def __init__(self):
        print('parent constructor')

    def m1(self):
        print('parent instance method')

class c(p):
    @classmethod
    def m2(cls):
        super(c,cls).__init__(cls)
        super(c,cls).m1(cls)

c.m2()