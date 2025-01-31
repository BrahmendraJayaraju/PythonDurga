#single inheritance 
class p:
    def m1(self):
        print('parent method')

class c(p):
    def m2(self):
        print('child method')

a=c()
a.m2()
a.m1()