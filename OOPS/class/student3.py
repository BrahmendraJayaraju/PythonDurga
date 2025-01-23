class student3:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def talk(self):
         print('my name is:', self.name)
         print('my rollno is:', self.rollno)
         print('my marks is:', self.marks)

s1=student3('brahmendra','212720597',90)
s2=student3('brahmendra','212720597',90)


s1.talk()
print('*'*30)
s2.talk()