class test:

    #this will sum
    def m1(selfself,*args):
        total=0
        totalarguments=0
        for x in args:
            total=total+x
            totalarguments= totalarguments+1
        print('the sum:',total)
        print('total arguments:',totalarguments)
        print()



t=test()
t.m1()
t.m1(10)
t.m1(10,20)
t.m1(10,20,30)