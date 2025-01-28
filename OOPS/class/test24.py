class test24:
    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        self.c=30

t=test24()
t.m1() #called and it adds
t.d=40  # adding through referencee variable
print(t.__dict__)