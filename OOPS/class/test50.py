#to del static variable , still m1 is not called so it will not del

class test50:
    a=10
    @classmethod
    def m1(cls):
        del test50.a

print(test50.__dict__)