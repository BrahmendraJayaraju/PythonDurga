#object created 
class test55:
    a=10
    def __init__(self):
        test55.b=20
        del test55.a

    def m1(self):
        test55.c=30
        del test55.b

    @classmethod
    def m2(cls):
        test55.d=40
        del test55.c

    @staticmethod
    def m3():
        test55.e=50
        del test55.d

t1=test55()
print(test55.__dict__)