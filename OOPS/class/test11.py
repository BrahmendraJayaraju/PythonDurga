class test11:
    def __init__(self):
        print('no arg constructir')

    def __init__(self,x):

        print('with arg constructir',x)

#t=test11() # error bse always last constructor is called while creating object
t=test11(10)
