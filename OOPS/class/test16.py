class student:
    school = 'durga soft'  # class variiable same for all object

    def __init__(self, name, rollno):
        self.name = name  # instance variable seperate copy for each object
        self.rollno = rollno


    def talk(self):
        x=10 #local variable
        for i in x:
            print(i)