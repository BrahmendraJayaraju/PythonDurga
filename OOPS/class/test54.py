#no object created so only a will be there in class
class test54:
    a=10
    def __init__(self):
        test54.b=20
        del test54.a

    def m1(self):
        test54.c=30
        del test54.b

    @classmethod
    def m2(cls):
        test54.d=40
        del test54.c

    @staticmethod
    def m3():
        test54.e=50
        del test54.d


print(test54.__dict__)