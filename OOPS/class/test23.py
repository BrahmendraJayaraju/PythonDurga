class test23:
    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        self.c=30

t=test23()
t.m1() #called and it adds

print(t.__dict__)
# a,b,c will be added to object instance variables