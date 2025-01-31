
#mul overloading in both class

class timesheet:
    def __init__(self,names,workingdays):
        self.name=names
        self.workingdays=workingdays

    def __mul__(self, other):
        #position is imp 
        return self.workingdays*other.salaryperday

class employee:
    def __init__(self,name,salaryperday):
        self.name=name
        self.salaryperday=salaryperday

    def __mul__(self, other):
        return self.salaryperday*other.workingdays


e=employee('durge',500)
t=timesheet('divya',25)

print('this month salary e :',e*t)

print('this month salary t :',t*e)

