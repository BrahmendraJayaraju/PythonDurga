class student19:
    school='durga'   # class variable

    def __init__(self,name,rollno):
        self.name=name  #instance variable
        self.rollno=rollno

    def getinfo(self):    #instance method
        print('my name is :',self.name)
        print('my rollno is :', self.rollno)

    @classmethod   #class method
    def getschoolinfo(cls):
        print('my school name is :',cls.school)


    @staticmethod
    def getsum(a,b):  # static method
        sum=a+b
        return sum
