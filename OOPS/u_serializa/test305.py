#wap to perform pickling and unpickling of employee object


import pickle

class employee:
    def __init__(self,eno,ename,esal,eddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eddr

    def display(self):
        print('employee number:{},ename:{},esal:{},eaddr:{}'.format(self.eno,self.ename,self.esal,self.eaddr))


e=employee(100,'Durga',1000,'hyd')
with open('emp.scr','wb') as f:
    pickle.dump(e,f)

with open('emp.scr','rb') as f:
    emp_obj=pickle.load(f)
    emp_obj.display()