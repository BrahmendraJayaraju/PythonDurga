import random
import time

names=['sunny','bunny','chinny','vinnay']
subjects=['python','java','datascience']



def studentslist(num):
    results=[]
    for i in range(num):
        student={'id':i,
                 'name':random.choice(names),
                 'subject':random.choice(subjects)}
        results.append(student)
        return results

#......................346 down......................

t1=time.time()
students=studentslist(100000)
t2=time.time()
print('total time taken in normal:',t2-t1)


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
print('total time taken in generator:',t2-t1)



