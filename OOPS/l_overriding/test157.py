#over riding demo program

class person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight

    def display(self):
        print('name:',self.name)
        print('age:',self.age)
        print('height',self.height)
        print('weight',self.weight)

class employee(person):
    def __init__(self,name,age,height,weight,eno,esal):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.eno=eno
        self.esal=esal


    def display(self):
        print('name:',self.name)
        print('age:',self.age)
        print('height',self.height)
        print('weight',self.weight)
        print('eno:',self.eno)
        print('esal:',self.esal)

e=employee('brahmendra',20,3,7,4234324,42342422)
e.display()