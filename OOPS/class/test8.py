class test8:
    def __init__(delf,name,rollno,marks,object):
        print('creating an instance variables and initializing for object {}'.format(object))
        delf.n=name
        delf.r=rollno
        delf.m=marks

    def talk(kelf):
        print('my name is:', kelf.n)
        print('my roll number :', kelf.r)
        print('my marks is :', kelf.m)

t1=test8('brahmendra','212720597',90,1)
t1.talk()


print('*'*30)
t2=test8('brahmendra2','2127205972',902,2)
t2.talk()
