#constructor overloading is not possible in python ,always takes last argument



class test:
    def __init__(self):
        print('no arg constructor')

    def __init__(self,x):
        print('1 arg constructor')

    def __init__(self, x,y):
         print('2 arg constructor')

#t=test()
#t=test(10)
t=test(10,20)
