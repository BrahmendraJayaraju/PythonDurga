class test:
    count=0
    def __init__(self):
        test.count=test.count+1


    @classmethod
    def getnoofobjects(cls):
        print('constructor called this times',test.count)

test.getnoofobjects()
t1=test()
t2=test()
t3=test()
t4=test()
t5=test()
t6=test()
test.getnoofobjects()