#recursion error 
class p:
    def m1(self):
        print('parent method')

class c(p):
    def m1(self):
        self.m1()
        print('child method')


a=c()
a.m1()