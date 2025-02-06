#demo program for serialization and deserialization by  using json pickle

import jsonpickle
class employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr

    def display(self):
        print('eno:{},ename:{},esal:{},eddr:{}'.format(self.eno,self.ename,self.ename,self.esal,self.eaddr))


e=employee(100,'durga',1000.0,'hyd')

#serialize object to json string directly
print('............serialize object to json string directly.......................')
json_string=jsonpickle.encode(e)
print(json_string)
print(type(json_string))

#serialize ti json file
with open('emp.json','w') as f:
    f.write(json_string)

print('...............................deseriali. from json string  ......................')
#desearialize from json string
e2=jsonpickle.decode(json_string)
print(e2)
print(type(e2))
e2.display()


print('...............................deseriali. from file ......................')
#desialize the json file
with open('emp.json','r') as f:
    meow=f.readline()
e3= jsonpickle.decode(meow)

print(e3)
print(type(e3))
e3.display()
