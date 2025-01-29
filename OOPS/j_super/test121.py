#use super()

class person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight

    def display(self):
        print('name :',self.name)
        print('age :', self.age)
        print('height :', self.height)
        print('weight :', self.weight)

class student(person):

    def __init__(self,name,age,height,weight,rollno,marks):
        super().__init__(name,age,height,weight)
        self.rollno=rollno
        self.marks=marks


    def display(self):
        super().display()
        print('rollno:', self.rollno)
        print('marks :', self.marks)

s=student('ravi',24,5.6,70,101,95)
s.display()

