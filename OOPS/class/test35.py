#access static variable from constructor 
class test35:
    a=10
    def __init__(self):
        print(self.a)
        print(test35.a)

t1=test35()
