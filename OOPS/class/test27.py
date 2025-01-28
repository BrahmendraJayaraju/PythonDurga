class test27:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40

    def m1(self):
        del self.c   #DELETING FROM INSIDE METHOD

t=test27()
t.m1()

print(t.__dict__)
print('*'*30)


#deleting from reference variable from outside class 
t2=test27()
del t2.a,t2.b
print(t2.__dict__)