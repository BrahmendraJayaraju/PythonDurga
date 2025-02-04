import json

#convert to json string format

employee={'name':'durga',
          'age':35,
          'salary':100.89,
          'is married':True,
          'is having GF':None}

#convert into json string
js=json.dumps(employee)
print(js)


#to print in vertical form in output
employee1={'name':'durga',
          'age':35,
          'salary':100.89,
          'is married':True, #observe in output
          'is having GF':None} #observe in output

#convert into json string
js1=json.dumps(employee1,indent=2)  #after 2 space
print(js1)