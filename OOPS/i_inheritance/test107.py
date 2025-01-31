#multilevel inheritance
class grandparent:
    def m1(self):
        print('grand parent method')

class parent(grandparent):
    def m2(self):
        print('parent method')

class child(parent):
    def m3(self):
        print('child method')

a=child()
a.m1()
a.m2()
a.m3()