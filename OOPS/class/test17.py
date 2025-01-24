class student17:
    school='durga'

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

        #instance method bse trying to access instance variable
    def getstudentdetails(self):
        print('student name :',self.name)
        print('student name :', self.rollno)
