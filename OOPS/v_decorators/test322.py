

def decor(func):
    def inner():
        print('send to beauty parlor')
        print('showing a persn with full make up')
    return inner

def display():
    print('show without makeup')

    
display()

