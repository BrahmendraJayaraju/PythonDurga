class test30:
    a=10
    def __init__(self):
        test30.b=20

    def m1(self):
        test30.c=30  # declaring inside method 



t=test30()   #b will be added to class
t.m1()# c will be added
print(test30.__dict__)