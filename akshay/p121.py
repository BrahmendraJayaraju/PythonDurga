a,b=10,20
def outer():
    global a,b
    print(a,b)
    def inner():
        global a,b
        print(a,b)
        
    inner()

outer()    
