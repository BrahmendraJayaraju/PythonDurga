#to serialize and deserialize multiple
import pickle

class employee:
    def __init__(self,eno,ename,esal,eddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eddr

    def display(self):
        print('employee number:{},ename:{},esal:{},eaddr:{}'.format(self.eno,self.ename,self.esal,self.eaddr))

