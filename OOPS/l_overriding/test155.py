
#parent class constructor is executed since child dont havbe used defined constructor
class parent:
    def __init__(self):
        print('parent constructor')


class child(parent):
    pass

c=child()
