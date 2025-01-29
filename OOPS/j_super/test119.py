#calling parent class method from child class using super()
class p:
    a=10
    def __init__(self):
        print('parent class constructor')

    def m1(self):
        print('parent instance method')

    @classmethod
    def m2(cls):
        print('parent class method')

    @staticmethod
    def m3():
        print('parent static method')

class c(p):
    def __init__(self):
        print('child class constructor')

    def method1(self):
        print('child instance method')
        print(super().a)
        super().m1()
        super().m2()
        super().m3()
        super().__init__()

a=c()
a.method1()
