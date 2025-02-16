import random
import time

names=['sunny','bunny','chinny','vinnay']
subjects=['python','java','datascience']



def studentslist(num):
    for i in range(num):
        student={'id':i,
                 'name':random.choice(names),
                 'subject':random.choice(subjects)}
        yield student



t1=time.time()
students=studentslist(100000)
t2=time.time()
print('total time taken:',t2-t1)