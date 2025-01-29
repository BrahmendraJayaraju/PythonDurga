class a:
    def m1(self):
        print('a class method')

class b(a):
    def m1(self):
        print('b class method')


class c(b):
    def m1(self):
        print('c class method')

class d(c):
    def m1(self):
        print('d class method')


class e(d):
    def m1(self):
        print('e class method')
        a.m1(self)  # to call method of particular super class
        #or
        super(d,self).m1()  #check this doubt 
z=e()
z.m1()