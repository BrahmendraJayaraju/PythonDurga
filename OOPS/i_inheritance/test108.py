#hierarchial inheritance
#one parent and multiple child
class parent:
    def m1(self):
        print('parent method')

class child1(parent):
    def m2(self):
        print('child 1 method')

class child2(parent):
    def m3(self):
        print('child 2 method')

a=child1()
a.m1()
a.m2()

b=child2()
b.m1()
b.m3()