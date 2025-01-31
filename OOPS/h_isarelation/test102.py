class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eatndrink(selfself):
        print('eat and drink juice')

class employee(person):
    def __init__(self,name,age,eno,esal):
        #self.name=name
        #self.age=age
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal


    def work(self):
        print('coding pyton program')

    def emploinfo(self):
        print(self.name)
        print(self.age)
        print(self.eno)
        print(self.esal)


e=employee('brahmendra',30,21217621,25715271212)
e.eatndrink()
e.work()
e.emploinfo()
