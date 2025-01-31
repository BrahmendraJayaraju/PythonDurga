class car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color

    def getinfo(self):
        print('car nameis:{},model:{},carcolor:{} '.format(self.name,self.model,self.color))


class employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car

    def empifo(self):
        print('employee name:',self.ename)
        print('employeem no:', self.eno)
        print('employee car:',self.car)
        self.car.getinfo()

c=car('inova','2.5v','grey')

emp=employee('brahmendra',7823283782,c)

emp.empifo()