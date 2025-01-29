#super() vs parent class instance variable
class p:
    a=888
    def __init__(self):
        self.b=999

class c(p):

    def __init__(self):
        self.b=20
    def m1(self):
        print(self.b)



a=c()
a.m1()