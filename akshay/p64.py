def isalpa(name):
    for i in name:
        if(ord(i) not in range(ord('A'),ord('Z')+1)) and (ord(i) not in range(ord('a'),ord('z')+1)):
            return False
    return True

                                                        
           
