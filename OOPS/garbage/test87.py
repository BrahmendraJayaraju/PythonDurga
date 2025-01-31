import time
class test87:
    def __init__(self):
        print('constructor')

    def __del__(self):
        print('destructor')

l=[test87(),test87(),test87()]

del l
time.sleep(3)
print('end of application')