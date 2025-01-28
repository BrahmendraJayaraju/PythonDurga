class test30:
    a=10
    def __init__(self):
        test30.b=20  # declaring inside method



print(test30.__dict__)


#since object not created b will not be shown in dict