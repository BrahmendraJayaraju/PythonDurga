class test46:
    def __init__(self):
        self.b=20

t1=test46()
t2=test46()

test46.a=888
t1.b=999
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)