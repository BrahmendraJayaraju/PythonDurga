#constructor over riding
class parent:
    def __init__(self):
        print('parent constructor ')


class child(parent):
    def __init__(self):
        print('child constructor ')
        #to call parent class constructor
        super().__init__()

c=child()