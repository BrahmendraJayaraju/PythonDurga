#print s1 internally calls string method __str__
class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

s1=student('durge',1013232323,95)
s2=student('brahmendra',323232323,56)

print(s1)
print(s2)

