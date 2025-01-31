#MRO algorith
class a:
    pass

class b:
    pass

class c:
    pass

class d(a,b):
    pass

class e(b,c):
    pass

class f(d,e,c):
    pass


print(a.mro())
print(b.mro())
print(c.mro())
print(d.mro())
print(e.mro())
print(f.mro()) #difficult to find this 