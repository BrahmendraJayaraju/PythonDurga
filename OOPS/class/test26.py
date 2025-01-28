class test26:
    def __init__(self):
        self.a=10
        self.b=20
    def display(self):
        print(self.a)  #accessing instance variable by using self from instance method 
        print(self.b)


t=test26()
t.display()

print('*'*30)
#accessing instance variable outside class by using reference variable of object
print(t.a)
print(t.b)
