class student:
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setmarks(self,marks):
        self.marks=marks
    def getmarks(self):
        return self.marks

a=int(input('enter the number of students:'))
students=[]

for i in range(a):
    name=input('enter the student name:')
    marks=int(input('enter the marks:'))
    s=student()
    s.setname(name)
    s.setmarks(marks)
    students.append(s)

for i in students:
    print(s.getname())
    print(s.getmarks())
