class engine:
    def __init__(self):
        self.power='125kw'

    def m1(self):
        print('engine specification')

class car:
    def __init__(self):
        self.engine=engine()

    def usecar(self):
        print('car required functionality')
        self.engine.m1()  #calling method of other class
        print(self.engine.power)

c=car()
c.usecar()