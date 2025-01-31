#we can access private member outside classs (secret )
#name mangling

class test:
    def __init__(self):
        self.__x=10

    def __m1(self):
        print('private method')

    def m2(self):
        print(self.__x)
        self.__m1()

t=test()

#to access private members outside class
print(t._test__x)
t._test__m1()
