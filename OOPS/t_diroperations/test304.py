import json
#explicit conversion  from object -> python dict -> json 
class employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr


    def display(self):
        print('eno:{},ename:{},esal:{},eddr:{}'.format(self.eno,self.ename,self.ename,self.esal,self.eaddr))


e=employee(100,'durga',1000.0,'hyd')



#convert this to python dict
a=e.__dict__
print(a)
print(type(a))

#serialization to json string
json_string=json.dumps(a,indent=2)
print(json_string)

#serialization to json file
with open('emp.json','w') as f:
    json.dump(a,f,indent=4)

#deserialization  from json file to python object -> employee object

with open('emp.json','r') as f:
    edict=json.load(f)

e=employee(edict['eno'],edict['ename'],edict['esal'],edict['eaddr'])

e.display()
print('........')
print(edict)
print(type(edict))





