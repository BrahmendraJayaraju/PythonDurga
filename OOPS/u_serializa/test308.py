import pickle
from test306 import employee

#multiple object serialization
#need to execyte 307 before this


#we ger ran out of input
f=open('emp.ser','rb')
#    emp_obj=pickle.load(f)
#    emp_obj.display()


while True:
    try:
        emp_obj=pickle.load(f)
        emp_obj.display()
    except:
        print('no more to print ')
        break






