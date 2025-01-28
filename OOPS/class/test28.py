class test28:
    def __init__(self):
        self.a=10
        self.b=20

t=test28()
t.a=888

t2=test28()

print('a:',t.a,'\n','b:',t.b)


print('*'*30)

print('a:',t2.a,'\n','b:',t2.b)

#every object has own copy so changing one will not affect other