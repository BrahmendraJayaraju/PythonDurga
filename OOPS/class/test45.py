class test45:
    a=10
    def __init__(self):
        self.b=20

t1=test45()
t2=test45()
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)


test45.a=888
test45.b=999
print('after changing')
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)
print('Test:',test45.a,test45.b)


