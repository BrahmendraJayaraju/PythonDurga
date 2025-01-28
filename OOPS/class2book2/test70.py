class math:
    @staticmethod
    def add(a,b):
        print('the sum is :',a+b)

    @staticmethod
    def mul(a, b):
        print('the mul is :', a * b)

    @staticmethod
    def average(a, b):
        print('the sum is :', a + b/2)

m=math()
print('by using reference variable')
m.add(2,3)
m.mul(2,3)
m.average(2,3)
print()
print('by using class name ')
math.add(2,3)
math.mul(2,3)
math.average(2,3)