#self should contain alwayd magic method
#mul overloading

class timesheet:
    def __init__(self,names,workingdays):
        self.name=names
        self.workingdays=workingdays

class employee:
    def __init__(self,name,salaryperday):
        self.name=name
        self.salaryperday=salaryperday

    def __mul__(self, other):
        return self.salaryperday*other.workingdays


e=employee('durge',500)
t=timesheet('divya',25)

print('this month salary:',e*t)

#t does not contain magic method in timesheet so error
print('this month salary:',t*e)

