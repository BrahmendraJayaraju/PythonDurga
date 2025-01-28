class test22:
    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        self.c=30

t=test22()
print(t.__dict__)


# a,b will be added to object instance variables