class bird:
    wings=6
    @classmethod
    def fly(cls, name):
        print('{} flywing with {} wings'.format(name,cls.wings))

bird.fly('parrot')
bird.fly("eagle")