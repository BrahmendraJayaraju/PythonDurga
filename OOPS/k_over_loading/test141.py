#string overriding __str__

class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def __str__(self):
        return 'ename:{},roll:{},marks:{}'.format(self.name,self.rollno,self.marks)

s1=student('durge',1013232323,95)
s2=student('brahmendra',323232323,56)


#s1.__str__
print(s1)
print(s2)