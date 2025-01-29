#super() vs parent class instance variable
class p:
    a=888
    def __init__(self):
        self.b=999

class c(p):
    def m1(self):
        print(self.a)
        print(self.b)
        #or
        print(super().a)
        print(super().b)#we cannot access parent clss insttance variable through super



a=c()
a.m1()