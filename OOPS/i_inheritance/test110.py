#if same method is inherited from both parent class then order of parent is considered

class parent1:
    def m1(self):
        print('parent 1 method')


class parent2:
    def m1(self):
        print('parent 2 method')


class child( parent2,parent1,):
    def m3(self):
        print('child method')


#m1 is common
a=child()
a.m1()
