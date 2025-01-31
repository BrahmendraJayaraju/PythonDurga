#MRO algorith
class a:
    def m1(self):
        print('a class method')

class b(a):
    def m1(self):
        print('b class method')

class c(a):
    def m1(self):
        print('c class method')

class d(b,c):
    def m1(self):
        print('d class method')

a=d()
print(d.mro())
a.m1()
