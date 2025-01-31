import time


class test84:
    def __init__(self):
        print('object initialization activity')

    def __del__(self):
        print('perform clean up activity like DB disconnection and network disconnection')

t=test84()
t=None
time.sleep(10) #after 10 seconds 

print('end of application')
