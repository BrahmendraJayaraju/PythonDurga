#access static variable from instance method
class test36:
    a=10
    def __init__(self):
        print(self.a)
        print(test36.a)

    def diaplay(self):
        print(self.a)
        print(test36.a)

t1=test36()
t1.diaplay()
