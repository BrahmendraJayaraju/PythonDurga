a,b=10,20
def outer():
    a,b=1,2
    def inner():
        print(a,b)
    print(a,b)
    inner()
    print(a,b)

print(a,b)
outer()
print(a,b)
