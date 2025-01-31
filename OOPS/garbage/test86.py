import time
class test86:
    def __init__(self):
        print('object initialization activity')

    def __del__(self):
        print('perform clean up activity like DB disconnection and network disconnection')

t1=test86()
t2=t1
t3=t1

del t1
time.sleep(4)
print('object not deleted after deleting t1')

del t2
time.sleep(4)
print('object not deleted after deleting t2')

del t3
time.sleep(4)
print('removing last ref t3')

print('end of application ')