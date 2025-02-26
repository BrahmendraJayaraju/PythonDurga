a,b=10,20
def outer():
    global a,b
    print(a,b)
    def inner():
        global a,b
        a,b=1,2
        
    inner()
    print(a,b)

outer()    
print(a,b)
