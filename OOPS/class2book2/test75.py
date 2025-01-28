#accessing members of one class inside another class
class test75:

    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal

    def display(self):
        print('employee number',self.eno)
        print('enter emp name',self.ename)
        print('enter the esal',self.esal)

class mananger:

    def updateempsal(emp):  #acts as self
        emp.esal=emp.esal+10000
        emp.display()

emp=test75(101,'brahmendra',1450000)
mananger.updateempsal(emp)  #passing ref variable
