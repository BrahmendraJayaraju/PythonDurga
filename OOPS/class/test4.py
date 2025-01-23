class test:

    def __init__(self):
        print('address of the self:',id(self))


t=test()
print('address of the object:',id(t))
#check output both address are same pointing to same object 
