#overloading of > and <= operator for student

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
s1=student('durge',100)
s2=student('brahmendra','99')

print(s1>s2)