def countinitialindex(name,key,start=0,end=0):
    if end==0:
        end=len(name)
    for i in range(start,end):
        if name[i]==key:
            return i
    return -1

c1=countinitialindex('hello world','w')


if(c1!=-1):
   print('element found at {} position'.format(c1))
else:
    print('element not found')
    
   
