#to check which type is passed inside method 
class test:
    def m1(self,x):
        print('{} argument method'.format(x.__class__.__name__))


t=test()
t.m1(10)
t.m1(10.5)
t.m1('brahmendra')