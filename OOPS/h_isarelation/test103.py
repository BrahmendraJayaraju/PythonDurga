class car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color

    def meowgetinfo(self):
        print('car:{},model:{},color:{}'.format(self.name,self.model,self.color))

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eatndrink(selfself):
        print('eat and drink juice')

class employee(person):

    def __init__(self,name,age,eno,esal,car):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal
        self.car=car

    def work(self):
        print('coding pyton program')

    def emploinfo(self):
        print(self.name)
        print(self.age)
        print(self.eno)
        print(self.esal)
        print('employee car information')
        self.car.meowgetinfo()

a=car('innove','2.5v','grey')

e=employee('brahmendra',48,434343,123232323,a)

e.eatndrink()
e.work()
e.emploinfo()

