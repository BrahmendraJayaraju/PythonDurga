a,b=10,20
def display():
    a,b=1,2
    print(a,b)

def swap():
    global a,b
    print(a,b)
    a,b=b,a


print(a,b)
display()
swap()
print(a,b)
