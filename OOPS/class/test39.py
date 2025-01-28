# access static variable from outside of class by object reference or by class name
class test39:
    a = 10

    def __init__(self):
        print(self.a)
        print(test39.a)

    def diaplay(self):
        print(self.a)
        print(test39.a)

    @classmethod
    def m2(cls):
        print(cls.a)
        print(test39.a)

    @staticmethod
    def m1():
        print(test39.a)

t1 = test39()
print('outside of class')
print(t1.a)
print(test39.a)


