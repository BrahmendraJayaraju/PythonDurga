class  person:
    def __init__(self,name,dd,mm,yyyy):
        print('person object creation')
        self.name=name
        self.dob=self.dob(dd,mm,yyyy)

    def info(self):
        print('name:',self.name)
        self.dob.display()

    class dob:

        def __init__(self,dd,mm,yyyy):
            print('dob object creation')
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy

        def display(self):
            print('dob={}/{}/{}'.format(self.dd,self.mm,self.yyyy))


p=person('brahmendra',23,2,1995)

p.info()