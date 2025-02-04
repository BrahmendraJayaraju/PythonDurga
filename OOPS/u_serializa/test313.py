#deserialize from  json file
#execite 311 first


# from json file to dict
import json

with open('emp.json','r') as f:
    employee=json.load(f)

print(type(employee))

for k,v in employee.items():
    print(k,':',v)