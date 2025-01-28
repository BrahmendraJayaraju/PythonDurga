##to del static variable  after calling m1 method
class test52:
    a=10
    @classmethod
    def m1(cls):
        del cls.a  # using cls

test52.m1()
print(test52.__dict__)