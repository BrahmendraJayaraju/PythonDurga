#to define a method with variable number of arguments
class test:
      def m1(self,*args):
          print('variable argument method')







t=test()
t.m1()
t.m1(10)
t.m1(10,20)
t.m1(10,20,30)