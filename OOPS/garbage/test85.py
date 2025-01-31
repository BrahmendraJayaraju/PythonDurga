import time
class test85:
    def __init__(self):
        print('object initialization activity')

    def __del__(self):
        print('perform clean up activity like DB disconnection and network disconnection')


t1=test85()
t2=test85()

print('end of application')