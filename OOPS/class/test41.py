#change static variable value from  instance method/class method /static method/outside class
class test41:
    a=10
    def __init__(self):
        test41.a=30

    def display(self):
        test41.a=40

    @classmethod
    def m1(cls):
        test41.a = 50
        cls.a=90

    @staticmethod
    def m2():
        test41.a=60


k=test41()
print('from constructor ',k.a)
print('from instance method ',k.display(),k.a)
print('from class ',k.m1(),test41.a)
print('from  static ',k.m2(),test41.a)

test41.a=212720597
print('from outside',test41.a)
