#how to call parent class static and class methods from child class static method 
class p:

    @classmethod
    def m2(cls):
        print('parent class method')

    @staticmethod
    def m3():
        print('parent static method')

class c(p):

    @staticmethod
    def m2():
        super(c,c).m2()
        super(c,c).m3()

c.m2()