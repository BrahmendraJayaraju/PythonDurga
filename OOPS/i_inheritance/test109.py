#multiple inheritance
#one child  and multiple parent
class parent1:
        def m1(self):
            print('parent 1 method')

class parent2:
    def m2(self):
        print('parent 2 method')

class child(parent1,parent2):
    def m3(self):
        print('child method')

a=child()
a.m1()
a.m2()
a.m3()