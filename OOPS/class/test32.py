#insdie class method by using cls otherwise classname

class test32:
    a=10
    def __init__(self):
        test32.b=20

    def m1(self):
        test32.c=30

    @classmethod
    def m2(cls):
        cls.d=40  #adding inside the class method 
        test32.e=50
t=test32()  # b added
t.m1()  # c added
t.m2()  #d,e added

print(test32.__dict__)
