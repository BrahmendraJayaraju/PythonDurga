def split(s,key=" ",n=0):
    if n==0:
        n=s.count(key)
    temp=['']
    j=0
    for i in s:
     if i==key and j<n:
        temp.append("")
        j=j+1
     else:
        temp[j]=temp[j]+i
    return temp

         
