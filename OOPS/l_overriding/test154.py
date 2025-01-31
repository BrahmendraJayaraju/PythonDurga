#method over riding
class parent:
    def property(self):
        print('land+gold+cash+power')

    def marry(self):
        print('appalamma')

class child(parent):
    def marry(self):
        print('kajal')

        #to calll parent class marry
        #super().marry()

c=child()
c.property()
c.marry()
