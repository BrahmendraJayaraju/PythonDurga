#method overloading  not supported in python
#always last method will be checked

class test:
    def m1(self):
        print('no arg method')

    def m1(self,x):
        print('one arg method')

    def m1(selfself,x,y):
        print('two arg method')

a=test()
# 1 arg missing error
#a.m1()
#a.m1(10)
a.m1(10,20)