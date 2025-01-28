#access static variable from class
class test37:
    a=10
    def __init__(self):
        print(self.a)
        print(test37.a)

    def diaplay(self):
        print(self.a)
        print(test37.a)

    @classmethod
    def m2(cls):
        print(cls.a)
        print(test37.a)
        

t1=test37()
t1.diaplay()
print('from class')
t1.m2()
test37.m2()
