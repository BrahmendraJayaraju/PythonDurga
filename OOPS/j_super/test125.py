#various important conclusion on super()
class p:
    def __init__(self):
        print('parent constructor')

    def m1(self):
        print('parent instance method')

    @classmethod
    def m2(cls):
        print('parent class method')

    @staticmethod
    def m3():
        print('parent static method')

class c(p):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    @classmethod
    def m2(cls):
        #super().__init__()
        #super().m1()
        super().m2()
        super().m3()

    @staticmethod
    def m3():
        pass
        #super().__init__()
        #super().m1()
        #super().m2()
        #super().m3()



a=c()
#a.m1()
#a.m2()
a.m3()