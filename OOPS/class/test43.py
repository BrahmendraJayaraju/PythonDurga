#check book modifying in class , not creating in instance variable
#since a is not in instance object it takes from class
class test43:
    a=10
    def m1(self):
        test43.a=888

t1=test43()
t1.m1()
print('taking from instance object ',t1.a)
print('taking from class',test43.a)