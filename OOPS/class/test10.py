class test10:
    def __init__(self):
        print('constructor executed')


#by default constructor will be there
t=test10()  # here once 
t.__init__()
t.__init__()
t.__init__()
t.__init__()

# total 5 times constructor is called
