class test49:
    a=10
    def __init__(self):
        self.b=20

    @classmethod
    def m1(cls):
        cls.a=888
        cls.b=999

t1=test49()
t2=test49()
t1.m1()

print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)
print('test:',test49.a,test49.b)

