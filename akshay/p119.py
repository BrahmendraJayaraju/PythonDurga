a,b=10,20
def outer():
    a,b=1,2
    def inner():
        print(a,b)
    inner()

outer()    
