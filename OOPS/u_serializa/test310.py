#to print in vertical form in output and sort in ascending order

import json
employee1={'name':'durga',
          'age':35,
          'salary':100.89,
          'is married':True, #observe in output
          'is having GF':None} #observe in output

#sort in ascending
js1=json.dumps(employee1,indent=2,sort_keys=True)  #after 2 space #false it will shuffle 
print(js1)