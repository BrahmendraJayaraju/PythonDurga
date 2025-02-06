from pyaml import yaml


emp_dict={'name':'brahmendra',
          'age':30,
          'salary':291722,
          'is married':False,
          'is having Gf':None
}

#convert to yaml string
yaml_str=yaml.dump(emp_dict)
print(yaml_str)
print(type(yaml_str))


#convert to yaml file
with open('emp.yaml','w') as f:
    yaml.dump(emp_dict,f)


#deserialize from yaml string to python dict

print('.......deserialize from string ..................')
ds_string=yaml.safe_load(yaml_str)
for k,v in ds_string.items():
    print(k,":",v)

##deserialize from yaml file to python dict
print('.......deserialize from  yaml file  ..................')
with open('emp.yaml','r') as f:
       ds_file=yaml.safe_load(f)
print(ds_file)









