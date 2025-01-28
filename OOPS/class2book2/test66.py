from tkinter.font import names


class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print('hi',self.name)
        print('your marks',self.marks)

    def grade(self):
        if self.marks>=60:
            print('you got A grade')
        elif  self.marks>=50:
            print('you got B grade')
        elif self.marks>=35:
            print('you got C grade')
        else:
            print('you got D grade')

n=int(input('number of students you want to entry'))
for i in range(n):
    name=input('enter student name ')
    marks=int(input('enter the marks'))
    s=student(name,marks)
    s.display()
    s.grade()
    print()

