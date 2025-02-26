


def reverse(name):
    rev=""
    for i in range(len(name)-1,-1,-1):
        rev=rev+name[i]
    return rev

def ispalindrome(name):
    revstring=reverse(name)
    print(revstring)
    if revstring==name:
     return True
    else:
     return False


if ispalindrome('malayalam'):
    print('yes pali')
else:
    print('not pali')
    
