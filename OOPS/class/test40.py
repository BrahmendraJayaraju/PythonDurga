
#change static variable value from constructor using class name
class test40:
    a=10
    def __init__(self):
        test40.a=30

k=test40()
print(k.a)