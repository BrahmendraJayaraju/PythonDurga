
#class and instance object with a  values
#since a is in object it takes from object 
class test42:
    a=10
    def m1(self):
        self.a=888

t1=test42()
t1.m1()
print('taking from instance object ',t1.a)
print('taking from class',test42.a)
