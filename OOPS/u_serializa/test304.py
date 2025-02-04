import pickle

#after execution check in folder

class employee:

    def __init__(self,a,b,c,d):
        pass




e=employee(100,'Durga',1000,'hyd')
with open('emp.scr','wb') as f:
    pickle.dump(e,f)

with open('emp.scr','rb') as f:
    emp_obj=pickle.load(f)
    print(emp_obj)

