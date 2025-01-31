class tooyoungexception(Exception):

    def __init__(self,msg):
        self.msg=msg

class toooldexception(Exception):

    def __init__(self,msg):
        self.msg=msg


age=int(input('enter your age:'))

if age>60:
   raise toooldexception('you look old ')
elif age<18:
    raise tooyoungexception('you look young ')
else:
    print('thanks for registration')


