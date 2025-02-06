

def decor(func):
    def inner():
        print('send the person to beauty parlour')
        print('showing a person with full of decoration ')

    return inner

@decor
def display():
    print('showing a person without anything')

display()