class p:
    def m1(self):
        print('parent method')

class c(p):
    def m1(self):
        super().m1()
        print('child method')


a=c()
a.m1()