class test25:
    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        self.c=30

t=test25()
t.m1() #called and it adds
t.d=40  # adding through referencee variable
print(t.__dict__)

print('*'*30)

t2=test25()
print(t2.__dict__)