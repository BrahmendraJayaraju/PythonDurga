class test63:
    def m1(self):
        a=10    #local variable of m1
        print(a)
    def m2(self):
        print(a)  # a is local variable of m1 we cannot access outside method m1


t=test63()
t.m1()
t.m2()  #error