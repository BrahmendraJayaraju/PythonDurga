
#constructor with defaulyt  arguments passing

class test:
    def __init__(self,a=None,b=None,c=None):
        print('constructor calling with 1/2/3/4 argument')


t=test()
t=test(10)
t=test(10,20)
t=test(10,20,30)

