a,b=10,20
def outer():
    a,b=1,2
    def inner():
        global a,b
        a,b=b,a
    print(a,b)
    inner()
    print(a,b)

print(a,b)
outer()
print(a,b)
