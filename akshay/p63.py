def ispal(name):
    n=len(name)
    for i in range(0,n//2+1):
        if name[i]!=name[n-1-i]:
         return False
        else:
            return True

if ispal("malayalam"):
    print('yes its')
else:
     print('no its not')
     

        
