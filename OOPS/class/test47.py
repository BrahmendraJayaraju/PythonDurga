class test47:
    a=10
    def __init__(self):
        self.b=20

    def m1(self):
        self.a=888
        self.b=999

t1=test47()
t2=test47()
t1.m1()
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)