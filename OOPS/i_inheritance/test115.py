#MRO ALGORITH 
class a:
    def m1(self):
        print('a method ')

class b:
    def m1(self):
        print('b method')

class c:
    def m1(self):
        print('c method')


class d(a,b):
    def m1(self):
        print('d method')

class e(a,c):
    def m1(self):
        print('e method')

class f(d,e):
    def m1(self):
        print('f method')

# we can play here
a1=f()
a1.m1()


