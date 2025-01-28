class test44:
    a=10
    def __init__(self):
        self.b=20


t1=test44()
t2=test44()
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)


t1.a=888
t1.b=999
print('after changing')
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)