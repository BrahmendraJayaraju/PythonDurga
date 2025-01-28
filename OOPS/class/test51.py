##to del static variable  after calling m1 method
class test51:
    a=10
    @classmethod
    def m1(cls):
        del test50.a # using class name

test51.m1()
print(test51.__dict__)