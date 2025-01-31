#<= magic method

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self,other):
        return self.marks>other.marks

    def __le__(self,other):
        return self.marks<=other.marks



s1 = student('durge', 100)
s2 = student('brahmendra', 99)


print(s1<=s2)