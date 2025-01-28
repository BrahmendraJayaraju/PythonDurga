#insdie class method by using cls otherwise classname

class test33:
    a=10
    def __init__(self):
        test33.b=20

    def m1(self):
        test33.c=30

    @classmethod
    def m2(cls):
        cls.d=40
        test33.e=50

    @staticmethod
    def m3():
        test33.f=90  #adding inside static method

t=test33()  # b added
t.m1()  # c added
t.m2()  #d,e added
t.m3()  # f added
print(test33.__dict__)
