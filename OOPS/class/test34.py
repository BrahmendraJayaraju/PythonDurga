class test34:
    a = 10

    def __init__(self):
        test34.b = 20

    def m1(self):
        test34.c = 30

    @classmethod
    def m2(cls):
        cls.d = 40
        test34.e = 50

    @staticmethod
    def m3():
        test34.f = 90  # adding inside static method


t = test34()  # b added
t.m1()  # c added
t.m2()  # d,e added
t.m3()  # f added

test34.g=70  #adding outside of class
print(test34.__dict__)
