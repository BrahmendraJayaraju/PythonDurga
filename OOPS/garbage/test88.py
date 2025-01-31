import time
class test88:
    def __init__(self):
        print('constructor')

    def __del__(self):
        print('destructor')

l=[test88(),test88(),test88()]
print('end of application')