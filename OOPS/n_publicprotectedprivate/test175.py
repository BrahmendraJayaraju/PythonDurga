class test:
    def __init__(self):
        self._x=10  #protected variable

    def m1(self):
        print(self._x)   #access protected variable within class

class subtest(test):
    def m2(self):
        print(self._x)   #access protected variable from child class


t=subtest()
t.m1()
t.m2()

#since we are accing from child class variable its possible
print(t._x)


#this is doubt 
a=test()
print(a._x)


