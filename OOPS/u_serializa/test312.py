#demo to deserialize the json string
#desrialize from java form to python

import json

#this is in java form see the quotes
json_string='''{"name":"durga",
               "age":35,
                "salary":100.0,
                "is married":true,
                "is having gf":null
               }'''
employee=json.loads(json_string)

print(type(employee))


print(employee['name'])
print(employee['age'])
print(employee['salary'])
print(employee['is married'])
print(employee['is having gf'])
#observe output true and none

#to print all at a time

for k,v in employee.items() :
    print(k,':',v)




