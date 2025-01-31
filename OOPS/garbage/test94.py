import sys
class test93:
    pass

t1=test93()
t2=t1
t3=t2
t4=t3

del t3,t4
print(sys.getrefcount(t1))