#to check how many arguments are passed


class test:

    def m1(self,a=None,b=None,c=None):
        if a is not None and b is not None and c is not None:
            print(' 3 argument method')
        elif  a is not None and b is not None:
            print(' 2 argument method')

        elif a is not None:
            print(' 1 argument method')

        else:
            print(' No argument method')

t=test()
#t.m1()
#t.m1(10)
#t.m1(10,20)
t.m1(10,20,30)
