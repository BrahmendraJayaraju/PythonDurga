class test72:

    def m1(x):
        print('some method')

t=test72()
t.m1()  # treated as instance method x is considered as self
t.m1(10)#error x,1o cant pass ,x  is treated as self

