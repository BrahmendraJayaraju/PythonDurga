# access static variable from static method
class test38:
    a = 10

    @staticmethod
    def m1():

        print(test38.a)




t1 = test38()
t1.m1()

