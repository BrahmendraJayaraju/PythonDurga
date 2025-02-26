def islower(name):
    for i in name:
        if(ord(i) in range (ord('A'),ord('Z')+1)):
           return False
    return True
