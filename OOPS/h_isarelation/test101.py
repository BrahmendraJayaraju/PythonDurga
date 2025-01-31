class p:
    a=10
    def __init__(self):
        print('paret constructor')
        self.b=20

    def m1(self):
        print('parent instance method')

    @classmethod
    def m2(cls):
        print('parent class method')

    @staticmethod
    def m3():
        print('parent static method')

class c(p):
    pass


d=c()
print(d.a)
print(d.b)
d.m1()
d.m2()
d.m3()


