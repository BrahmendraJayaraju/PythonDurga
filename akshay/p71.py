def startswith(name,sub,start=3,end=8):
    if end==0:
        end=len(name)
    if(end-start)<len(sub):
        return False
    j=0
    for i in range(start,start+len(sub)):
         if name[i]!=sub[j]:
            return False
         j=j+1
    return True       
         
