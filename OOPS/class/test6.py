


class test6:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def talk(self):
        print('my name is:',self.name)
        print('my roll number :',self.rollno)
        print('my marks is :',self.marks)

t=test6('brahmendra','212720597',90)
t.talk()