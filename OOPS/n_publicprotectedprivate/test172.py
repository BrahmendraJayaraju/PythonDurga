#public method ex


class Test:

    def __init__(self):
        self.x=10      #by default this is public instance variable

    def m1(self):     #public method
        print('public method')

    def m2(self):
        print(self.x)   # call within class variable
        self.m1()   # call within class (method)

t=Test()
t.m1()     #calling method from outside class
t.m2()
print(t.x)  #calling  variable from outside class

