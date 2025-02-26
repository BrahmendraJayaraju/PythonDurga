def endswith(name,sub,start=0,end=0):
    if end==0:
        end=len(name)
    if(end-start)<len(sub):
        return False
    j=0
    for i in range(end-len(sub),end):
         if name[i]!=sub[j]:
            return False
         j=j+1
    return True
