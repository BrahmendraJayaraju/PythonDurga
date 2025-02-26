def isupper(name):
    for i in name:
        if(ord(i) in range(ord('a'),ord('z')+1)):
           return False
    return True
    
