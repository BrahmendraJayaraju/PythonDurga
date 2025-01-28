#del static variable outside class

class test53:
    a=10
    @classmethod
    def m1(cls):
        del cls.a

del test53.a
print(test53.__dict__)


