a,b=10,20
def outer():
    a,b=1,2
    print(a,b)
    def inner():
        global a,b
        print(a,b)
        
    inner()

outer()    
