#private method ex


class Test:

    def __init__(self):
        self.__x=10      #private variable

    def __m1(self):     #private  method
        print('public method')

    def m2(self):        #public method
        print(self.__x)   # call within class  private variable
        self.__m1()   # call within class (private method)

t=Test()
#t.__m1()     #calling private method from outside class (error)
t.m2()     #calling public method outside class works
#print(t.__x)  #calling  private variable from outside class (error)

