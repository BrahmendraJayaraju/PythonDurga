
def isalpa(name):
    for i in name:
        if(ord(i) not in range(ord('0'),ord('9')+1)):
            return False
    return True 
